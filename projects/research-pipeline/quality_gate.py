#!/usr/bin/env python3
"""
Research Report Quality Gate — Stage 1 (Deterministic)
Checks encoding, formatting, citations, structure against hybrid APA/McKinsey standard.
Usage: python3 quality_gate.py <report.md|report.html> [--strict] [--fix] [--json]
Exit code 0 = PASS, 1 = FAIL, 2 = WARN (issues found but not blocking)
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Optional


# === CONSTANTS ===

FORBIDDEN_CHAR_RANGES: list[tuple[int, int, str]] = [
    (0xE000, 0xF8FF, "Private Use Area"),
    (0xFFFD, 0xFFFD, "Replacement Character"),
    (0x2318, 0x2318, "Command Key ⌘"),
    (0x2325, 0x2325, "Option Key ⌥"),
    (0x21E7, 0x21E7, "Shift Symbol ⇧"),
]

LLM_PHRASES: list[str] = [
    "I'd be happy to", "Great question", "Absolutely", "I think",
    "It's worth noting", "It's important to note", "In conclusion",
    "Let me", "I'll", "I can", "Here's", "Sure thing",
    "As an AI", "As a language model", "I don't have personal",
    "Certainly!", "Of course!", "That's a great",
    "Delve", "Tapestry", "Landscape", "Synergy", "Leverage",
    "Cutting-edge", "Game-changer", "Paradigm shift",
]

APPLE_FONTS: list[str] = ["-apple-system", "BlinkMacSystemFont", "SF Pro"]

APA_CITATION_RE = re.compile(r'\(([A-Z][a-zà-ÿ]+(?:\s(?:et\sal\.|&\s[A-Z][a-zà-ÿ]+))*),\s\d{4}[a-z]?\)')
NAKED_URL_RE = re.compile(r'(?<!\()\bhttps?://[^\s)\]>]+')
HEADING_MD_RE = re.compile(r'^(#{1,6})\s+(.+)', re.MULTILINE)


# === DATA STRUCTURES ===

class Issue:
    """A single quality gate issue."""
    def __init__(self, severity: str, line: int, description: str, category: str) -> None:
        self.severity = severity  # CRITICAL, ERR, WARN
        self.line = line
        self.description = description
        self.category = category

    def to_dict(self) -> dict[str, Any]:
        return {"severity": self.severity, "line": self.line, "description": self.description}


class CheckResult:
    """Result of a single check category."""
    def __init__(self, name: str) -> None:
        self.name = name
        self.issues: list[Issue] = []

    @property
    def status(self) -> str:
        severities = {i.severity for i in self.issues}
        if "CRITICAL" in severities or "ERR" in severities:
            return "FAIL"
        if "WARN" in severities:
            return "WARN"
        return "PASS"

    def to_dict(self) -> dict[str, Any]:
        return {"status": self.status, "issues": [i.to_dict() for i in self.issues]}


# === HTML PARSER ===

class ReportHTMLParser(HTMLParser):
    """Extract text, headings, styles, meta from HTML."""
    def __init__(self) -> None:
        super().__init__()
        self.tags_stack: list[str] = []
        self.unclosed: list[str] = []
        self.headings: list[tuple[int, str, int]] = []  # (level, text, line)
        self.text_lines: list[tuple[str, int]] = []  # (text, line)
        self.styles: list[str] = []
        self.has_viewport: bool = False
        self.has_print_css: bool = False
        self.images_without_alt: list[int] = []
        self.has_position_fixed_inline: bool = False
        self.has_back_cover_text: bool = False
        self._current_text: str = ""
        self._current_line: int = 1
        self._in_style: bool = False
        self._style_content: str = ""
        self._in_ref_section: bool = False
        self.all_text: str = ""
        self.font_families: list[tuple[str, int]] = []

        self.VOID_ELEMENTS = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        line = self.getpos()[0]
        attr_dict = dict(attrs)

        if tag not in self.VOID_ELEMENTS:
            self.tags_stack.append(tag)

        if tag == 'meta' and attr_dict.get('name') == 'viewport':
            self.has_viewport = True

        if tag == 'style':
            self._in_style = True
            self._style_content = ""

        if tag == 'img' and not attr_dict.get('alt'):
            self.images_without_alt.append(line)

        m = re.match(r'h(\d)', tag)
        if m:
            self._current_text = ""
            self._current_line = line

    def handle_endtag(self, tag: str) -> None:
        if tag in self.VOID_ELEMENTS:
            return
        if self.tags_stack and self.tags_stack[-1] == tag:
            self.tags_stack.pop()
        # Don't track unclosed aggressively - HTML is lenient

        m = re.match(r'h(\d)', tag)
        if m:
            self.headings.append((int(m.group(1)), self._current_text.strip(), self._current_line))

        if tag == 'style':
            self._in_style = False
            self.styles.append(self._style_content)
            if '@media print' in self._style_content:
                self.has_print_css = True
            if 'position:fixed' in self._style_content.replace(' ', '') or 'position: fixed' in self._style_content:
                self.has_position_fixed_inline = True
            for ff_match in re.finditer(r'font-family\s*:\s*([^;}{]+)', self._style_content):
                self.font_families.append((ff_match.group(1), self.getpos()[0]))

    def handle_data(self, data: str) -> None:
        line = self.getpos()[0]
        if self._in_style:
            self._style_content += data
            return
        self._current_text += data
        self.all_text += data + "\n"
        self.text_lines.append((data, line))
        if "AI Strategy" in data and "Research" in data:
            self.has_back_cover_text = True


# === CHECK FUNCTIONS ===

def _is_forbidden(cp: int) -> Optional[str]:
    """Check if a codepoint is in the forbidden ranges."""
    for start, end, name in FORBIDDEN_CHAR_RANGES:
        if start <= cp <= end:
            return name
    return None


def check_encoding(lines: list[str]) -> CheckResult:
    """Check for forbidden Unicode characters."""
    result = CheckResult("encoding")
    for i, line in enumerate(lines, 1):
        for j, ch in enumerate(line):
            name = _is_forbidden(ord(ch))
            if name:
                result.issues.append(Issue(
                    "CRITICAL", i,
                    f"Forbidden char U+{ord(ch):04X} ({name}) at col {j+1}",
                    "encoding"
                ))
    return result


def check_citations_md(lines: list[str], text: str) -> CheckResult:
    """Check citation format for Markdown."""
    result = CheckResult("citations")
    ref_section_start = None
    for i, line in enumerate(lines):
        if re.match(r'^#{1,2}\s+(?:References?|Sources?|Bibliography)', line, re.IGNORECASE):
            ref_section_start = i
            break

    # Find in-text citations
    in_text_citations: set[str] = set()
    for m in APA_CITATION_RE.finditer(text):
        in_text_citations.add(m.group(1).split(",")[0].strip())

    # Naked URLs in body (not in references section)
    for i, line in enumerate(lines, 1):
        if ref_section_start and i > ref_section_start:
            continue
        for m in NAKED_URL_RE.finditer(line):
            # Skip if inside parentheses or markdown link
            result.issues.append(Issue("WARN", i, f"Naked URL in body: {m.group()[:60]}...", "citations"))

    if in_text_citations and ref_section_start is None:
        result.issues.append(Issue("ERR", 0, "In-text citations found but no References section", "citations"))

    return result


def check_citations_html(parser: ReportHTMLParser, lines: list[str]) -> CheckResult:
    """Check citations in HTML using extracted text."""
    return check_citations_md(lines, parser.all_text)


def check_structure_md(lines: list[str], text: str) -> CheckResult:
    """Check document structure for Markdown."""
    result = CheckResult("structure")
    headings: list[tuple[int, str, int]] = []
    for i, line in enumerate(lines, 1):
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            headings.append((len(m.group(1)), m.group(2).strip(), i))

    _check_structure_common(result, headings, text)
    return result


def check_structure_html(parser: ReportHTMLParser) -> CheckResult:
    """Check document structure for HTML."""
    result = CheckResult("structure")
    _check_structure_common(result, parser.headings, parser.all_text)

    if not parser.has_back_cover_text:
        result.issues.append(Issue("WARN", 0, "Back cover text not found (expected 'AI Strategy · ... · Research')", "structure"))

    return result


def _check_structure_common(result: CheckResult, headings: list[tuple[int, str, int]], text: str) -> None:
    """Common structure checks."""
    # H1 count
    h1s = [h for h in headings if h[0] == 1]
    if len(h1s) == 0:
        result.issues.append(Issue("ERR", 0, "No H1 (title) found", "structure"))
    elif len(h1s) > 1:
        result.issues.append(Issue("WARN", h1s[1][2], f"Multiple H1s found ({len(h1s)})", "structure"))

    # Executive Summary
    exec_sum = None
    for h in headings:
        if "executive summary" in h[1].lower():
            exec_sum = h
            break
    if not exec_sum:
        result.issues.append(Issue("ERR", 0, "No Executive Summary section found", "structure"))

    # Heading hierarchy: no H3 without prior H2
    seen_h2 = False
    for level, title, line in headings:
        if level == 2:
            seen_h2 = True
        if level == 3 and not seen_h2:
            result.issues.append(Issue("ERR", line, f"H3 '{title}' without prior H2", "structure"))

    # Empty sections (heading followed immediately by another heading)
    for i in range(len(headings) - 1):
        _, title, line = headings[i]
        next_line = headings[i + 1][2]
        if next_line - line <= 2 and headings[i][0] >= headings[i + 1][0]:
            result.issues.append(Issue("WARN", line, f"Possibly empty section: '{title}'", "structure"))

    # Confidence score check
    confidence_found = bool(re.search(r'(?i)confidence[:\s]+\d+%', text))
    if not confidence_found:
        result.issues.append(Issue("WARN", 0, "No confidence score found in report", "structure"))


def check_content(lines: list[str], text: str, strict: bool = False) -> CheckResult:
    """Check content quality."""
    result = CheckResult("content")

    # LLM phrases
    for i, line in enumerate(lines, 1):
        for phrase in LLM_PHRASES:
            if phrase.lower() in line.lower():
                # Context-sensitive: "landscape" alone in a word is fine, as standalone buzzword = flag
                if phrase.lower() in ("landscape", "delve", "synergy", "leverage", "tapestry",
                                       "cutting-edge", "game-changer", "paradigm shift"):
                    # Only flag if used as buzzword (not part of longer technical context)
                    words = line.lower().split()
                    if phrase.lower() in words:
                        result.issues.append(Issue("ERR", i, f'LLM phrase: "{phrase}"', "content"))
                else:
                    result.issues.append(Issue("ERR", i, f'LLM phrase: "{phrase}"', "content"))

    # Long sections without subheadings
    headings_lines: list[int] = []
    for i, line in enumerate(lines, 1):
        if re.match(r'^#{1,6}\s+', line) or re.match(r'<h[1-6]', line, re.IGNORECASE):
            headings_lines.append(i)

    max_words = 500 if strict else 1000
    for idx in range(len(headings_lines)):
        start = headings_lines[idx]
        end = headings_lines[idx + 1] if idx + 1 < len(headings_lines) else len(lines)
        section_text = " ".join(lines[start:end])
        word_count = len(section_text.split())
        if word_count > max_words:
            result.issues.append(Issue(
                "ERR" if strict else "WARN", start,
                f"Section at line {start} has {word_count} words without subheading (max {max_words})",
                "content"
            ))

    return result


def check_html_specific(parser: ReportHTMLParser, lines: list[str]) -> CheckResult:
    """HTML-specific checks."""
    result = CheckResult("html")

    # Apple fonts
    for ff, line in parser.font_families:
        for af in APPLE_FONTS:
            if af.lower() in ff.lower():
                result.issues.append(Issue("WARN", line, f"Apple system font found: {af}", "html"))
                break

    # Viewport
    if not parser.has_viewport:
        result.issues.append(Issue("WARN", 0, "No <meta name='viewport'> found", "html"))

    # Print CSS
    if not parser.has_print_css:
        result.issues.append(Issue("WARN", 0, "No @media print CSS rules found", "html"))

    # Position fixed
    if parser.has_position_fixed_inline:
        result.issues.append(Issue("WARN", 0, "Inline style with position:fixed (breaks print)", "html"))

    # Images without alt
    for line in parser.images_without_alt:
        result.issues.append(Issue("WARN", line, "Image without alt text", "html"))

    return result


# === FIX FUNCTIONS ===

def fix_content(content: str, is_html: bool) -> str:
    """Apply automatic fixes and return fixed content."""
    # Remove forbidden chars
    chars_out: list[str] = []
    for ch in content:
        if _is_forbidden(ord(ch)):
            chars_out.append(" ")
        else:
            chars_out.append(ch)
    content = "".join(chars_out)

    # Replace Apple fonts
    if is_html:
        content = re.sub(
            r"font-family\s*:\s*[^;}{]*(?:-apple-system|BlinkMacSystemFont|SF Pro)[^;}{]*",
            "font-family: 'Georgia', 'Times New Roman', serif",
            content, flags=re.IGNORECASE
        )

    return content


# === MAIN ===

def run_gate(filepath: str, strict: bool = False, fix: bool = False, json_output: bool = False) -> int:
    """Run the quality gate on a report file. Returns exit code."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        return 1

    content = path.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()
    is_html = path.suffix.lower() in (".html", ".htm")

    results: list[CheckResult] = []

    # 1. Encoding
    results.append(check_encoding(lines))

    # 2. Citations
    if is_html:
        parser = ReportHTMLParser()
        parser.feed(content)
        results.append(check_citations_html(parser, lines))
    else:
        results.append(check_citations_md(lines, content))

    # 3. Structure
    if is_html:
        results.append(check_structure_html(parser))
    else:
        results.append(check_structure_md(lines, content))

    # 4. Content
    results.append(check_content(lines, content, strict))

    # 5. HTML-specific
    if is_html:
        results.append(check_html_specific(parser, lines))

    # Strict mode: promote WARN to ERR
    if strict:
        for r in results:
            for issue in r.issues:
                if issue.severity == "WARN":
                    issue.severity = "ERR"

    # Compute totals
    critical = sum(1 for r in results for i in r.issues if i.severity == "CRITICAL")
    errors = sum(1 for r in results for i in r.issues if i.severity == "ERR")
    warnings = sum(1 for r in results for i in r.issues if i.severity == "WARN")

    if critical > 0 or errors > 0:
        verdict = "FAIL"
    elif warnings > 0:
        verdict = "WARN"
    else:
        verdict = "PASS"

    # Fix mode
    if fix:
        fixed = fix_content(content, is_html)
        fixed_path = path.with_name(f"{path.stem}_fixed{path.suffix}")
        fixed_path.write_text(fixed, encoding="utf-8")
        print(f"Fixed version written to: {fixed_path}")

    # Output
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if json_output:
        out = {
            "report": path.name,
            "timestamp": now,
            "verdict": verdict,
            "score": {"critical": critical, "errors": errors, "warnings": warnings},
            "checks": {r.name: r.to_dict() for r in results},
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        _print_fancy(path.name, now, results, verdict, critical, errors, warnings)

    if verdict == "FAIL":
        return 1
    elif verdict == "WARN":
        return 2
    return 0


def _print_fancy(name: str, timestamp: str, results: list[CheckResult],
                 verdict: str, critical: int, errors: int, warnings: int) -> None:
    """Print the fancy box output."""
    W = 50
    def pad(s: str) -> str:
        # strip ANSI for length calc is not needed here
        visible = s
        return s + " " * max(0, W - 4 - len(visible))

    icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌"}
    verdict_icon = {"PASS": "✅ PASS", "WARN": "⚠️  WARN", "FAIL": "❌ FAIL"}

    print("╔" + "═" * (W - 2) + "╗")
    print("║" + pad("  QUALITY GATE — Stage 1 (Deterministic)") + "║")
    print("╠" + "═" * (W - 2) + "╣")
    print("║" + pad(f"  Report: {name}") + "║")
    dt = timestamp[:16].replace("T", " ")
    print("║" + pad(f"  Date: {dt}") + "║")
    print("╠" + "═" * (W - 2) + "╣")
    print("║" + " " * (W - 2) + "║")

    for r in results:
        ic = icon.get(r.status, "?")
        count = len(r.issues)
        line = f"  {r.name.upper():<16} {ic} {r.status} ({count} issues)"
        print("║" + pad(line) + "║")

    print("║" + " " * (W - 2) + "║")
    print("╠" + "═" * (W - 2) + "╣")
    print("║" + pad(f"  VERDICT: {verdict_icon[verdict]}") + "║")
    print("║" + pad(f"  CRITICAL: {critical}  ERRORS: {errors}  WARNINGS: {warnings}") + "║")
    print("║" + " " * (W - 2) + "║")

    all_issues = [(i, r.name) for r in results for i in r.issues]
    if all_issues:
        print("║" + pad("  Details:") + "║")
        for issue, cat in all_issues[:20]:
            sev = {"CRITICAL": "CRIT", "ERR": "ERR", "WARN": "WARN"}[issue.severity]
            loc = f"Line {issue.line}: " if issue.line > 0 else ""
            detail = f"  [{sev}] {loc}{issue.description}"
            # Truncate long lines
            if len(detail) > W - 4:
                detail = detail[:W - 7] + "..."
            print("║" + pad(detail) + "║")

    print("╚" + "═" * (W - 2) + "╝")


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Research Report Quality Gate — Stage 1")
    parser.add_argument("report", help="Path to report file (.md or .html)")
    parser.add_argument("--strict", action="store_true", help="Strict mode: WARN becomes FAIL")
    parser.add_argument("--fix", action="store_true", help="Generate fixed version")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    exit_code = run_gate(args.report, strict=args.strict, fix=args.fix, json_output=args.json)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
