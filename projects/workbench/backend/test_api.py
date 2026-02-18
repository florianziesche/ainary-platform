"""
API Tests for Execution Platform Backend
Run: python3 test_api.py
"""
import requests
import json
import sys

API = "http://localhost:8080/api"
passed = 0
failed = 0
errors = []

def test(name, fn):
    global passed, failed
    try:
        fn()
        passed += 1
        print(f"  ✓ {name}")
    except AssertionError as e:
        failed += 1
        errors.append(f"  ✗ {name}: {e}")
        print(f"  ✗ {name}: {e}")
    except Exception as e:
        failed += 1
        errors.append(f"  ✗ {name}: {type(e).__name__}: {e}")
        print(f"  ✗ {name}: {type(e).__name__}: {e}")

# ── Topics ──
print("\n📋 Topics")

def test_list_topics():
    r = requests.get(f"{API}/topics")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0, "No topics found"

def test_get_topic():
    r = requests.get(f"{API}/topics/glasswing")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "glasswing"
    assert "name" in data
    assert "messages" in data
    assert "steps" in data

def test_get_topic_404():
    r = requests.get(f"{API}/topics/nonexistent-topic-xyz")
    assert r.status_code == 404

def test_create_and_delete_topic():
    # Create
    r = requests.post(f"{API}/topics", json={"id": "test-topic-42", "name": "Test Topic", "stage": "research", "meta": {}})
    assert r.status_code == 200
    # Verify
    r = requests.get(f"{API}/topics/test-topic-42")
    assert r.status_code == 200
    assert r.json()["name"] == "Test Topic"
    # Delete
    r = requests.delete(f"{API}/topics/test-topic-42")
    assert r.status_code == 200
    # Verify deleted
    r = requests.get(f"{API}/topics/test-topic-42")
    assert r.status_code == 404

def test_update_topic():
    r = requests.patch(f"{API}/topics/glasswing", json={"state": "active"})
    assert r.status_code == 200

test("List topics", test_list_topics)
test("Get topic", test_get_topic)
test("Get topic 404", test_get_topic_404)
test("Create and delete topic", test_create_and_delete_topic)
test("Update topic", test_update_topic)

# ── Messages ──
print("\n💬 Messages")

def test_post_message():
    r = requests.post(f"{API}/topics/glasswing/messages", json={"sender": "human", "content": "Test message", "msg_type": "text"})
    assert r.status_code == 200
    data = r.json()
    assert "id" in data

test("Post message", test_post_message)

# ── Corrections ──
print("\n🔧 Corrections")

def test_list_corrections():
    r = requests.get(f"{API}/corrections")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0, "No corrections found"
    assert "rule" in data[0]
    assert "severity" in data[0]

def test_create_correction():
    r = requests.post(f"{API}/corrections", json={"rule": "Test rule - delete me", "category": "test", "severity": 1})
    assert r.status_code == 200
    assert "id" in r.json()

def test_corrections_by_category():
    r = requests.get(f"{API}/corrections?category=design")
    assert r.status_code == 200
    data = r.json()
    assert all(c["category"] == "design" for c in data)

test("List corrections", test_list_corrections)
test("Create correction", test_create_correction)
test("Filter by category", test_corrections_by_category)

# ── Pre-Flight ──
print("\n🛫 Pre-Flight")

def test_preflight():
    r = requests.get(f"{API}/preflight/glasswing")
    assert r.status_code == 200
    data = r.json()
    assert "total_checks" in data
    assert "passed" in data
    assert "failed" in data
    assert "overall" in data
    assert data["overall"] in ("pass", "warn", "fail")
    assert data["total_checks"] == data["passed"] + data["warned"] + data["failed"]

def test_preflight_404():
    r = requests.get(f"{API}/preflight/nonexistent-xyz")
    assert r.status_code == 404

def test_preflight_layers():
    """Pre-flight returns layer info and structured results."""
    r = requests.get(f"{API}/preflight/glasswing")
    data = r.json()
    assert "layers_run" in data
    assert 1 in data["layers_run"]
    assert 2 in data["layers_run"]
    assert "skipped" in data
    for check in data["checks"]:
        assert "layer" in check or check.get("type") == "standard"
        assert check["status"] in ("pass", "warn", "fail")

def test_preflight_catches_llm_slop():
    """Pre-flight catches LLM phrases in output."""
    import time
    # Inject slop — use a dedicated test topic to avoid ordering issues
    requests.post(f"{API}/topics", json={"id": "test-slop-check", "name": "Slop Test", "stage": "research", "meta": {}})
    requests.post(f"{API}/topics/test-slop-check/messages", json={
        "sender": "mia", "content": "Great question! I'd be happy to help. This holistic game-changer is seamless.", "msg_type": "text"
    })
    time.sleep(0.2)
    r = requests.get(f"{API}/preflight/test-slop-check")
    data = r.json()
    # Cleanup
    requests.delete(f"{API}/topics/test-slop-check")
    assert data["failed"] > 0, f"Expected failures for LLM slop, got {data['failed']} checks:{[(c['rule'][:30],c['status']) for c in data['checks']]}"
    assert data["overall"] == "fail"

def test_preflight_clean_pass():
    """Clean output passes all checks."""
    requests.post(f"{API}/topics/glasswing/messages", json={
        "sender": "mia", "content": "Nächster Schritt: Email Draft vorbereiten. Confidence: 85%.", "msg_type": "text"
    })
    r = requests.get(f"{API}/preflight/glasswing")
    data = r.json()
    assert data["failed"] == 0, f"Clean output should pass, but {data['failed']} failed"

test("Pre-flight check", test_preflight)
test("Pre-flight 404", test_preflight_404)
test("Pre-flight layers", test_preflight_layers)
test("Pre-flight clean pass", test_preflight_clean_pass)
test("Pre-flight catches LLM slop", test_preflight_catches_llm_slop)

# ── Trust ──
print("\n🛡️ Trust")

def test_trust_skills():
    r = requests.get(f"{API}/trust/skills")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "skill" in data[0]
    assert "score" in data[0]
    assert all(0 <= s["score"] <= 100 for s in data)

def test_trust_feedback():
    r = requests.post(f"{API}/trust/skills/research/feedback", json={"direction": "up", "weight": 1})
    assert r.status_code == 200

def test_trust_bayesian():
    """Trust uses Bayesian scoring — multiple ups should increase score, downs decrease more."""
    # Get initial score
    r1 = requests.get(f"{API}/trust/skills")
    initial = {s["skill"]: s["score"] for s in r1.json()}
    
    # Give 3 ups to research
    for _ in range(3):
        requests.post(f"{API}/trust/skills/research/feedback", json={"direction": "up", "weight": 1})
    
    r2 = requests.get(f"{API}/trust/skills")
    after_ups = {s["skill"]: s["score"] for s in r2.json()}
    assert after_ups.get("research", 0) >= initial.get("research", 0), "Score should increase after ups"
    
    # Give 2 downs
    for _ in range(2):
        requests.post(f"{API}/trust/skills/research/feedback", json={"direction": "down", "weight": 1})
    
    r3 = requests.get(f"{API}/trust/skills")
    after_downs = {s["skill"]: s["score"] for s in r3.json()}
    assert after_downs.get("research", 0) < after_ups.get("research", 0), "Score should decrease after downs"

test("Trust skills", test_trust_skills)
test("Trust feedback", test_trust_feedback)
test("Trust Bayesian scoring", test_trust_bayesian)

# ── Folders ──
print("\n📁 Folders")

def test_list_folders():
    r = requests.get(f"{API}/folders")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

test("List folders", test_list_folders)

# ── Events ──
print("\n📝 Events")

def test_events():
    r = requests.get(f"{API}/events/glasswing")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)

test("Get events", test_events)

# ── Actions ──
print("\n⚡ Actions")

def test_action_queue():
    r = requests.post(f"{API}/actions/queue", json={"topic_id": "glasswing", "action_type": "test_action", "params": {}})
    assert r.status_code == 200
    assert r.json()["status"] == "queued"

def test_pending_actions():
    r = requests.get(f"{API}/actions/pending")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_email_validation():
    r = requests.post(f"{API}/actions/send-email", json={"to": "not-an-email", "subject": "Test", "body": "Test body here"})
    assert r.status_code == 400, f"Expected 400 for invalid email, got {r.status_code}"

def test_email_short_body():
    r = requests.post(f"{API}/actions/send-email", json={"to": "test@test.com", "subject": "Test", "body": "Hi"})
    assert r.status_code == 400, f"Expected 400 for short body, got {r.status_code}"

test("Queue action", test_action_queue)
test("Pending actions", test_pending_actions)
test("Email validation - bad address", test_email_validation)
test("Email validation - short body", test_email_short_body)

# ── AI ──
print("\n🤖 AI")

def test_ai_chat_no_key():
    # Only test if no key is set (won't actually call API)
    r = requests.post(f"{API}/ai/chat", json={"message": "test", "topic_id": "glasswing"})
    # Either 200 (key works) or 500 (no key) — both valid
    assert r.status_code in (200, 500)

test("AI chat endpoint exists", test_ai_chat_no_key)

# ── Pipeline ──
print("\n📊 Pipeline")

def test_pipeline():
    r = requests.get(f"{API}/pipeline")
    assert r.status_code == 200
    data = r.json()
    assert "stages" in data
    assert "total_items" in data

test("Pipeline stats", test_pipeline)

print(f"\n🏥 Health")
def test_health():
    r = requests.get(f"{API}/health")
    data = r.json()
    assert data["version"] == "0.10.0"
    assert "error_topics" in data

def test_health_counts():
    r = requests.get(f"{API}/health")
    assert r.json()["topics"] > 0

test("Health endpoint", test_health)
test("Health counts", test_health_counts)

print(f"\n🔄 State Machine")
def test_state_valid():
    requests.post(f"{API}/topics/glasswing/state", json={"state": "running"})
    r = requests.post(f"{API}/topics/glasswing/state", json={"state": "active"})
    assert r.status_code == 200

def test_state_invalid():
    requests.post(f"{API}/topics/glasswing/state", json={"state": "running"})
    r = requests.post(f"{API}/topics/glasswing/state", json={"state": "archived"})
    assert r.status_code == 409
    requests.post(f"{API}/topics/glasswing/state", json={"state": "active"})

def test_state_bad_value():
    r = requests.post(f"{API}/topics/glasswing/state", json={"state": "banana"})
    assert r.status_code == 400

def test_state_error_recovery():
    requests.post(f"{API}/topics/glasswing/state", json={"state": "running"})
    requests.post(f"{API}/topics/glasswing/state", json={"state": "error"})
    r = requests.post(f"{API}/topics/glasswing/state", json={"state": "active"})
    assert r.status_code == 200

test("Valid state transition", test_state_valid)
test("Invalid transition blocked", test_state_invalid)
test("Bad state value rejected", test_state_bad_value)
test("Error recovery", test_state_error_recovery)

print(f"\n🔁 Retry")
def test_retry_404():
    r = requests.post(f"{API}/actions/retry", json={"topic_id": "glasswing", "action_type": "nope"})
    assert r.status_code == 404

def test_fail_retry_cycle():
    requests.post(f"{API}/actions/queue", json={"topic_id": "glasswing", "action_type": "test_retry", "params": {}})
    requests.post(f"{API}/actions/complete", json={"topic_id": "glasswing", "action_type": "test_retry", "error": "fail"})
    r = requests.post(f"{API}/actions/retry", json={"topic_id": "glasswing", "action_type": "test_retry"})
    assert r.status_code == 200
    assert r.json()["retry"] == 1
    requests.post(f"{API}/actions/complete", json={"topic_id": "glasswing", "action_type": "test_retry", "result": "ok"})

test("Retry non-existent 404", test_retry_404)
test("Fail + retry cycle", test_fail_retry_cycle)

print(f"\n🌉 Mia Bridge")
def test_mia_no_task():
    r = requests.post(f"{API}/mia/execute", json={"task": ""})
    assert r.status_code == 400

def test_mia_streams():
    r = requests.post(f"{API}/mia/execute", json={"task": "Sag test", "topic_id": "glasswing"}, stream=True, timeout=15)
    assert r.status_code == 200
    assert "text/event-stream" in r.headers.get("content-type", "")
    got_data = False
    for line in r.iter_lines(decode_unicode=True):
        if line and line.startswith("data: "):
            got_data = True
            break
    r.close()
    assert got_data

test("Mia empty task rejected", test_mia_no_task)
test("Mia bridge streams", test_mia_streams)

print(f"\n🧠 Findings (CKE)")
def test_finding_create():
    r = requests.post(f"{API}/findings", json={
        "claim": "Test finding for automated tests",
        "confidence": 0.60,
        "tags": ["test", "automated"],
        "source_type": "own_data"
    })
    assert r.status_code == 200
    data = r.json()
    assert "id" in data
    assert data["confidence"] == 0.60

def test_finding_create_empty_claim():
    r = requests.post(f"{API}/findings", json={"claim": ""})
    assert r.status_code == 400

def test_finding_list():
    r = requests.get(f"{API}/findings")
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert "compound_score" in data[0]
    assert isinstance(data[0]["tags"], list)

def test_finding_get():
    r = requests.get(f"{API}/findings/RF-001")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "RF-001"
    assert "confidence_history" in data

def test_finding_get_404():
    r = requests.get(f"{API}/findings/RF-999")
    assert r.status_code == 404

def test_finding_update():
    # Get current
    r1 = requests.get(f"{API}/findings/RF-001")
    old_conf = r1.json()["confidence"]
    # Update confidence
    r = requests.put(f"{API}/findings/RF-001", json={
        "confidence": 0.90,
        "confidence_reason": "test update"
    })
    assert r.status_code == 200
    assert "compound_score" in r.json()
    # Verify history
    r2 = requests.get(f"{API}/findings/RF-001")
    assert len(r2.json()["confidence_history"]) >= 2

def test_finding_validate():
    # Create a fresh low-confidence finding for clean validation
    r0 = requests.post(f"{API}/findings", json={
        "claim": "Low conf finding for validation test",
        "confidence": 0.30,
        "tags": ["validation_test"],
        "source_type": "own_hypothesis"
    })
    fid = r0.json()["id"]
    r = requests.post(f"{API}/findings/{fid}/validate", json={
        "direction": "support",
        "source_type": "revenue_validated",
        "reason": "Confirmed by actual revenue"
    })
    assert r.status_code == 200
    data = r.json()
    # revenue_validated weight=0.90: new = 0.30*0.7 + 0.90*0.3 = 0.48 > 0.30
    assert data["new_confidence"] > data["old_confidence"]

def test_finding_contradict():
    r = requests.post(f"{API}/findings/RF-003/validate", json={
        "direction": "contradict",
        "source_type": "own_data",
        "reason": "Our data shows regex wins"
    })
    assert r.status_code == 200
    data = r.json()
    assert data["new_confidence"] < 0.40

def test_finding_related():
    r = requests.get(f"{API}/findings/RF-001/related")
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert "shared_tags" in data[0]

def test_finding_contradiction_detection():
    """Creating a finding with overlapping tags flags potential contradictions."""
    r = requests.post(f"{API}/findings", json={
        "claim": "Test contradiction detection",
        "tags": ["ai_quality", "pre_flight", "test_only"],
        "confidence": 0.50
    })
    data = r.json()
    assert "potential_contradictions" in data
    # Cleanup
    # (no delete endpoint yet, but tests are additive)

def test_findings_stats():
    r = requests.get(f"{API}/findings-stats")
    assert r.status_code == 200
    data = r.json()
    assert "total" in data
    assert "alive" in data
    assert "orphans" in data
    assert "research_lines" in data

def test_topic_findings():
    r = requests.get(f"{API}/topics/glasswing/findings")
    assert r.status_code == 200

test("Create finding", test_finding_create)
test("Create finding empty claim", test_finding_create_empty_claim)
test("List findings", test_finding_list)
test("Get finding", test_finding_get)
test("Get finding 404", test_finding_get_404)
test("Update finding + confidence history", test_finding_update)
test("Validate finding (support)", test_finding_validate)
test("Validate finding (contradict)", test_finding_contradict)
test("Related findings", test_finding_related)
test("Contradiction detection on create", test_finding_contradiction_detection)
test("Findings stats", test_findings_stats)
test("Topic findings", test_topic_findings)

print(f"\n🛡️ Error Handling")
def test_ai_chat_preflight():
    """AI chat returns auto pre-flight results."""
    r = requests.post(f"{API}/ai/chat", json={"message": "Sag test", "topic_id": "glasswing"}, timeout=30)
    if r.status_code == 200:
        data = r.json()
        assert "preflight" in data, "AI chat should include auto pre-flight"
        assert "overall" in data["preflight"]

def test_malformed_json():
    """Server handles malformed JSON gracefully."""
    r = requests.post(f"{API}/topics", data="not json", headers={"Content-Type": "application/json"})
    assert r.status_code == 422  # FastAPI validation error

def test_empty_body():
    """Server handles missing required fields."""
    r = requests.post(f"{API}/topics", json={})
    assert r.status_code == 422

def test_xss_in_topic_name():
    """XSS in topic name is stored as-is (frontend must escape)."""
    xss = '<script>alert("xss")</script>'
    r = requests.post(f"{API}/topics", json={"id": "test-xss", "name": xss, "stage": "research", "meta": {}})
    assert r.status_code == 200
    r2 = requests.get(f"{API}/topics/test-xss")
    assert r2.json()["name"] == xss  # Stored literally, not executed
    requests.delete(f"{API}/topics/test-xss")

def test_long_message():
    """Very long messages are accepted."""
    long_msg = "A" * 10000
    r = requests.post(f"{API}/topics/glasswing/messages", json={"sender": "human", "content": long_msg, "msg_type": "text"})
    assert r.status_code == 200

def test_state_on_nonexistent_topic():
    r = requests.post(f"{API}/topics/doesnt-exist/state", json={"state": "active"})
    assert r.status_code == 404

def test_preflight_on_empty_topic():
    """Pre-flight on topic with no messages handles gracefully."""
    requests.post(f"{API}/topics", json={"id": "test-empty-pf", "name": "Empty", "stage": "research", "meta": {}})
    r = requests.get(f"{API}/preflight/test-empty-pf")
    assert r.status_code == 200
    assert r.json()["has_output"] == False
    requests.delete(f"{API}/topics/test-empty-pf")

def test_double_complete():
    """Completing an already-completed action doesn't crash."""
    requests.post(f"{API}/actions/queue", json={"topic_id": "glasswing", "action_type": "dbl_test", "params": {}})
    requests.post(f"{API}/actions/complete", json={"topic_id": "glasswing", "action_type": "dbl_test", "result": "ok"})
    r = requests.post(f"{API}/actions/complete", json={"topic_id": "glasswing", "action_type": "dbl_test", "result": "ok again"})
    assert r.status_code == 200  # Idempotent, no crash

def test_concurrent_state_changes():
    """Rapid state changes don't corrupt."""
    import concurrent.futures
    def change(state):
        # Each tries a valid sequence
        requests.post(f"{API}/topics/glasswing/state", json={"state": "running"})
        requests.post(f"{API}/topics/glasswing/state", json={"state": "active"})
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        futures = [ex.submit(change, s) for s in range(3)]
        concurrent.futures.wait(futures)
    # Should still be in a valid state
    r = requests.get(f"{API}/topics/glasswing")
    assert r.json()["state"] in {"active", "running", None}

test("AI chat includes pre-flight", test_ai_chat_preflight)
test("Malformed JSON handled", test_malformed_json)
test("Empty body rejected", test_empty_body)
test("XSS stored safely", test_xss_in_topic_name)
test("Long message accepted", test_long_message)
test("State on nonexistent topic", test_state_on_nonexistent_topic)
test("Pre-flight on empty topic", test_preflight_on_empty_topic)
test("Double complete idempotent", test_double_complete)
test("Concurrent state changes safe", test_concurrent_state_changes)

# ── Results ──
print(f"\n{'='*40}")
print(f"Results: {passed} passed, {failed} failed, {passed+failed} total")
if errors:
    print("\nFailures:")
    for e in errors:
        print(e)
sys.exit(1 if failed else 0)
