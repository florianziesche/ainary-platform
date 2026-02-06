#!/usr/bin/env python3
"""
LinkedIn Network Analysis Script
Performs comprehensive primary research on Florian's LinkedIn network
"""

import csv
import json
from datetime import datetime
from collections import Counter, defaultdict
import re
from typing import Dict, List, Tuple

class LinkedInAnalyzer:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.connections = []
        self.load_data()
    
    def load_data(self):
        """Load and parse the LinkedIn connections CSV"""
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            # Skip the notes at the beginning - read until we find the header
            lines = f.readlines()
            
            # Find the header line
            header_index = None
            for i, line in enumerate(lines):
                if line.startswith('First Name'):
                    header_index = i
                    break
            
            if header_index is None:
                raise ValueError("Could not find header row in CSV")
            
            # Parse from header onwards
            from io import StringIO
            csv_content = ''.join(lines[header_index:])
            reader = csv.DictReader(StringIO(csv_content))
            
            for row in reader:
                self.connections.append(row)
        
        print(f"✅ Loaded {len(self.connections)} connections")
    
    def parse_date(self, date_str: str) -> datetime:
        """Parse LinkedIn date format: '05 Feb 2026'"""
        if not date_str or date_str.strip() == '':
            return None
        try:
            return datetime.strptime(date_str.strip(), '%d %b %Y')
        except:
            return None
    
    def analyze_connection_velocity(self) -> Dict:
        """ANALYSIS 1: Connection growth over time"""
        dates = []
        for conn in self.connections:
            date = self.parse_date(conn.get('Connected On', ''))
            if date:
                dates.append(date)
        
        dates.sort()
        
        # Group by month
        monthly = defaultdict(int)
        quarterly = defaultdict(int)
        yearly = defaultdict(int)
        
        for date in dates:
            month_key = date.strftime('%Y-%m')
            quarter_key = f"{date.year}-Q{(date.month-1)//3 + 1}"
            year_key = str(date.year)
            
            monthly[month_key] += 1
            quarterly[quarter_key] += 1
            yearly[year_key] += 1
        
        # Find spikes (months with >100 connections)
        spikes = [(k, v) for k, v in sorted(monthly.items(), key=lambda x: x[1], reverse=True)[:10]]
        
        # Recent activity (last 3 months)
        recent_months = sorted(monthly.items())[-3:]
        
        # Growth trend
        if len(dates) > 0:
            first_date = dates[0]
            last_date = dates[-1]
            total_days = (last_date - first_date).days
            avg_per_day = len(dates) / max(total_days, 1)
        else:
            first_date = last_date = None
            avg_per_day = 0
        
        return {
            'total_connections': len(self.connections),
            'connections_with_dates': len(dates),
            'date_range': {
                'first': first_date.strftime('%Y-%m-%d') if first_date else None,
                'last': last_date.strftime('%Y-%m-%d') if last_date else None,
                'span_days': total_days if first_date else 0
            },
            'growth_rate': {
                'avg_per_day': round(avg_per_day, 2),
                'avg_per_month': round(avg_per_day * 30, 1)
            },
            'monthly': dict(sorted(monthly.items())),
            'quarterly': dict(sorted(quarterly.items())),
            'yearly': dict(sorted(yearly.items())),
            'spikes': spikes,
            'recent_months': recent_months
        }
    
    def extract_industry(self, company: str, position: str) -> str:
        """Categorize industry based on company and position keywords"""
        text = f"{company} {position}".lower()
        
        # VC and Investment
        if any(kw in text for kw in ['venture', 'vc ', ' vc', 'capital', 'investor', 'investment', 'fund', 'angel']):
            return 'VC/Investment'
        
        # Startup/Founder
        if any(kw in text for kw in ['founder', 'co-founder', 'ceo', 'startup', 'entrepreneur']):
            return 'Startup/Founder'
        
        # AI/ML
        if any(kw in text for kw in ['artificial intelligence', 'machine learning', 'ai ', ' ai', 'ml ', ' ml', 'deep learning']):
            return 'AI/ML'
        
        # SaaS/Software
        if any(kw in text for kw in ['saas', 'software', 'platform', 'app', 'tech', 'digital']):
            return 'SaaS/Software'
        
        # Manufacturing
        if any(kw in text for kw in ['manufactur', 'cnc', 'engineering', 'industrial', 'production', 'factory']):
            return 'Manufacturing'
        
        # Corporate/Enterprise
        if any(kw in text for kw in ['corporation', 'enterprise', 'global', 'international', 'group']):
            return 'Corporate'
        
        # Consulting
        if any(kw in text for kw in ['consult', 'advisor', 'advisory']):
            return 'Consulting'
        
        # Finance
        if any(kw in text for kw in ['bank', 'finance', 'financial', 'private equity', 'hedge fund']):
            return 'Finance'
        
        # Academia/Research
        if any(kw in text for kw in ['university', 'research', 'professor', 'phd', 'academic']):
            return 'Academia/Research'
        
        return 'Other'
    
    def analyze_industry_clusters(self) -> Dict:
        """ANALYSIS 2: Industry distribution and company clusters"""
        companies = Counter()
        industries = Counter()
        
        vc_count = 0
        founder_count = 0
        corporate_count = 0
        manufacturing_count = 0
        
        for conn in self.connections:
            company = conn.get('Company', '').strip()
            position = conn.get('Position', '').strip()
            
            if company:
                companies[company] += 1
            
            industry = self.extract_industry(company, position)
            industries[industry] += 1
            
            # Detailed counting
            text = f"{company} {position}".lower()
            if any(kw in text for kw in ['venture', 'vc ', ' vc', 'capital', 'investor', 'investment', 'fund', 'angel']):
                vc_count += 1
            if any(kw in text for kw in ['founder', 'co-founder', 'ceo', 'startup', 'entrepreneur']):
                founder_count += 1
            if any(kw in text for kw in ['corporation', 'enterprise', 'global', 'international']):
                corporate_count += 1
            if any(kw in text for kw in ['manufactur', 'cnc', 'engineering', 'industrial']):
                manufacturing_count += 1
        
        total = len(self.connections)
        
        return {
            'top_companies': companies.most_common(30),
            'industry_distribution': dict(industries.most_common(20)),
            'percentages': {
                'VC': round(vc_count / total * 100, 1),
                'Founders': round(founder_count / total * 100, 1),
                'Corporate': round(corporate_count / total * 100, 1),
                'Manufacturing': round(manufacturing_count / total * 100, 1)
            },
            'network_composition_score': {
                'ai_saas_focus': round((industries.get('AI/ML', 0) + industries.get('SaaS/Software', 0)) / total * 100, 1),
                'vc_ecosystem': round(vc_count / total * 100, 1),
                'founder_density': round(founder_count / total * 100, 1)
            }
        }
    
    def extract_seniority(self, position: str) -> str:
        """Categorize seniority level from position title"""
        pos = position.lower()
        
        # C-level
        if any(kw in pos for kw in ['ceo', 'cto', 'cfo', 'coo', 'cmo', 'chief', 'founder', 'co-founder', 'president']):
            return 'C-Level/Founder'
        
        # VP
        if any(kw in pos for kw in ['vp ', ' vp', 'vice president']):
            return 'VP'
        
        # Director/Head
        if any(kw in pos for kw in ['director', 'head of', 'lead']):
            return 'Director/Head'
        
        # Manager
        if any(kw in pos for kw in ['manager', 'managing']):
            return 'Manager'
        
        # Senior
        if 'senior' in pos or 'sr.' in pos:
            return 'Senior'
        
        # Associate/Analyst
        if any(kw in pos for kw in ['associate', 'analyst', 'assistant', 'coordinator']):
            return 'Associate/Analyst'
        
        # Individual contributor
        if any(kw in pos for kw in ['engineer', 'developer', 'designer', 'consultant', 'specialist']):
            return 'IC (Individual Contributor)'
        
        return 'Other'
    
    def analyze_titles(self) -> Dict:
        """ANALYSIS 3: Title and seniority distribution"""
        seniority = Counter()
        founder_count = 0
        c_level_count = 0
        
        for conn in self.connections:
            position = conn.get('Position', '').strip()
            if not position:
                seniority['No Title'] += 1
                continue
            
            level = self.extract_seniority(position)
            seniority[level] += 1
            
            pos_lower = position.lower()
            if any(kw in pos_lower for kw in ['founder', 'co-founder']):
                founder_count += 1
            if any(kw in pos_lower for kw in ['ceo', 'cto', 'cfo', 'coo', 'cmo', 'chief']):
                c_level_count += 1
        
        total = len(self.connections)
        decision_makers = seniority.get('C-Level/Founder', 0) + seniority.get('VP', 0) + seniority.get('Director/Head', 0)
        
        return {
            'seniority_distribution': dict(seniority.most_common()),
            'percentages': {level: round(count / total * 100, 1) for level, count in seniority.items()},
            'founder_density': round(founder_count / total * 100, 1),
            'c_level_percentage': round(c_level_count / total * 100, 1),
            'decision_maker_percentage': round(decision_makers / total * 100, 1)
        }
    
    def analyze_network_gaps(self, industry_data: Dict, title_data: Dict) -> Dict:
        """ANALYSIS 4: Identify gaps based on Ainary Ventures thesis"""
        # Ainary thesis: AI + vertical SaaS + European founders
        
        gaps = []
        recommendations = []
        
        # Check for LP/Family office presence
        lp_count = sum(1 for c in self.connections if any(kw in f"{c.get('Company', '')} {c.get('Position', '')}".lower() 
                       for kw in ['limited partner', 'lp', 'family office', 'endowment', 'pension']))
        
        if lp_count < 50:
            gaps.append('Limited Partners / Family Offices')
            recommendations.append(f"Add {50-lp_count}+ LP connections for fundraising pipeline")
        
        # Manufacturing tech
        mfg_tech = sum(1 for c in self.connections if any(kw in f"{c.get('Company', '')} {c.get('Position', '')}".lower() 
                       for kw in ['manufacturing', 'cnc', 'industrial iot', 'factory', 'production tech']))
        
        if mfg_tech < 100:
            gaps.append('Manufacturing Tech Founders')
            recommendations.append(f"Target {100-mfg_tech}+ manufacturing/industrial tech connections")
        
        # European founders (rough heuristic)
        european_keywords = ['berlin', 'london', 'paris', 'amsterdam', 'munich', 'stockholm', 'zurich', 'copenhagen']
        european_count = sum(1 for c in self.connections if any(kw in f"{c.get('Company', '')}".lower() for kw in european_keywords))
        
        if european_count < 200:
            gaps.append('European Founders')
            recommendations.append(f"Expand European founder network by {200-european_count}+")
        
        # AI vertical SaaS
        ai_saas = sum(1 for c in self.connections if 
                     (any(kw in f"{c.get('Company', '')} {c.get('Position', '')}".lower() for kw in ['ai', 'ml', 'machine learning']) and
                      any(kw in f"{c.get('Company', '')} {c.get('Position', '')}".lower() for kw in ['saas', 'software', 'platform'])))
        
        return {
            'identified_gaps': gaps,
            'recommendations': recommendations,
            'current_coverage': {
                'LPs/Family Offices': lp_count,
                'Manufacturing Tech': mfg_tech,
                'European Founders': european_count
            }
        }
    
    def analyze_email_intelligence(self) -> Dict:
        """ANALYSIS 5: Email availability and reachability"""
        with_email = sum(1 for c in self.connections if c.get('Email Address', '').strip())
        without_email = len(self.connections) - with_email
        
        # Email by industry
        industry_emails = defaultdict(lambda: {'total': 0, 'with_email': 0})
        
        for conn in self.connections:
            company = conn.get('Company', '').strip()
            position = conn.get('Position', '').strip()
            industry = self.extract_industry(company, position)
            has_email = bool(conn.get('Email Address', '').strip())
            
            industry_emails[industry]['total'] += 1
            if has_email:
                industry_emails[industry]['with_email'] += 1
        
        # Calculate percentages
        industry_email_rates = {}
        for industry, counts in industry_emails.items():
            rate = counts['with_email'] / counts['total'] * 100 if counts['total'] > 0 else 0
            industry_email_rates[industry] = {
                'total': counts['total'],
                'with_email': counts['with_email'],
                'email_rate': round(rate, 1)
            }
        
        return {
            'total_connections': len(self.connections),
            'with_email': with_email,
            'without_email': without_email,
            'email_percentage': round(with_email / len(self.connections) * 100, 1),
            'reachable_network': with_email,
            'industry_email_rates': dict(sorted(industry_email_rates.items(), 
                                                key=lambda x: x[1]['email_rate'], reverse=True))
        }
    
    def identify_clusters(self) -> Dict:
        """ANALYSIS 6: Network power metrics and clusters"""
        # VC Lab cluster
        vc_lab = [c for c in self.connections if any(kw in f"{c.get('Company', '')} {c.get('Position', '')}".lower() 
                  for kw in ['vc lab', 'venture lab', 'venture institute', 'venture fellow'])]
        
        # Manufacturing cluster
        manufacturing = [c for c in self.connections if any(kw in f"{c.get('Company', '')} {c.get('Position', '')}".lower() 
                        for kw in ['manufactur', 'cnc', 'machining', 'industrial', 'factory', 'production'])]
        
        # Geographic distribution (rough heuristics)
        nyc_keywords = ['new york', 'nyc', 'manhattan', 'brooklyn']
        germany_keywords = ['germany', 'berlin', 'munich', 'hamburg', 'frankfurt', 'cologne']
        
        nyc_count = sum(1 for c in self.connections if any(kw in f"{c.get('Company', '')}".lower() for kw in nyc_keywords))
        germany_count = sum(1 for c in self.connections if any(kw in f"{c.get('Company', '')}".lower() for kw in germany_keywords))
        global_count = len(self.connections) - nyc_count - germany_count
        
        return {
            'vc_lab_cluster': {
                'count': len(vc_lab),
                'percentage': round(len(vc_lab) / len(self.connections) * 100, 1),
                'sample': [f"{c.get('First Name', '')} {c.get('Last Name', '')} - {c.get('Position', '')}" 
                          for c in vc_lab[:5]]
            },
            'manufacturing_cluster': {
                'count': len(manufacturing),
                'percentage': round(len(manufacturing) / len(self.connections) * 100, 1),
                'sample': [f"{c.get('First Name', '')} {c.get('Last Name', '')} - {c.get('Company', '')}" 
                          for c in manufacturing[:5]]
            },
            'geographic_distribution': {
                'NYC': {'count': nyc_count, 'percentage': round(nyc_count / len(self.connections) * 100, 1)},
                'Germany': {'count': germany_count, 'percentage': round(germany_count / len(self.connections) * 100, 1)},
                'Global/Other': {'count': global_count, 'percentage': round(global_count / len(self.connections) * 100, 1)}
            }
        }
    
    def analyze_timing_intelligence(self) -> Dict:
        """ANALYSIS 7: Timing patterns and growth periods"""
        dates = []
        day_of_week = Counter()
        
        for conn in self.connections:
            date = self.parse_date(conn.get('Connected On', ''))
            if date:
                dates.append(date)
                day_of_week[date.strftime('%A')] += 1
        
        # Hot periods (top months)
        monthly = defaultdict(int)
        for date in dates:
            month_key = date.strftime('%Y-%m')
            monthly[month_key] += 1
        
        hot_periods = sorted(monthly.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Calculate acceptance patterns (day of week)
        if len(dates) > 0:
            day_percentages = {day: round(count / len(dates) * 100, 1) for day, count in day_of_week.items()}
        else:
            day_percentages = {}
        
        return {
            'day_of_week_distribution': dict(day_of_week.most_common()),
            'day_percentages': day_percentages,
            'hot_periods': hot_periods,
            'peak_month': hot_periods[0] if hot_periods else None,
            'connection_patterns': {
                'weekday_total': sum(day_of_week[day] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
                'weekend_total': sum(day_of_week[day] for day in ['Saturday', 'Sunday'])
            }
        }
    
    def run_full_analysis(self) -> Dict:
        """Run all analyses and return comprehensive results"""
        print("\n🔍 RUNNING LINKEDIN NETWORK ANALYSIS\n")
        
        print("📊 Analysis 1: Connection Velocity...")
        velocity = self.analyze_connection_velocity()
        
        print("🏢 Analysis 2: Industry Clusters...")
        industries = self.analyze_industry_clusters()
        
        print("👔 Analysis 3: Title Analysis...")
        titles = self.analyze_titles()
        
        print("🎯 Analysis 4: Network Gaps...")
        gaps = self.analyze_network_gaps(industries, titles)
        
        print("📧 Analysis 5: Email Intelligence...")
        emails = self.analyze_email_intelligence()
        
        print("🔗 Analysis 6: Network Power Metrics...")
        clusters = self.identify_clusters()
        
        print("⏰ Analysis 7: Timing Intelligence...")
        timing = self.analyze_timing_intelligence()
        
        print("\n✅ Analysis complete!\n")
        
        return {
            'connection_velocity': velocity,
            'industry_clusters': industries,
            'title_analysis': titles,
            'network_gaps': gaps,
            'email_intelligence': emails,
            'network_power_metrics': clusters,
            'timing_intelligence': timing
        }

def main():
    csv_path = '/tmp/Connections.csv'
    
    print("=" * 70)
    print("LINKEDIN NETWORK ANALYSIS - PRIMARY RESEARCH")
    print("=" * 70)
    
    analyzer = LinkedInAnalyzer(csv_path)
    results = analyzer.run_full_analysis()
    
    # Save raw results to JSON
    output_json = '/Users/florianziesche/.openclaw/workspace/assets/tools/linkedin-analysis-results.json'
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"📄 Raw results saved to: {output_json}")
    
    return results

if __name__ == '__main__':
    main()
