import requests

BASE = "http://PROD_OR_STAGING_HOST:8080"  # Jenkins can replace this env at runtime

def test_index_status():
    r = requests.get(f"{BASE}/")
    assert r.status_code == 200
    j = r.json()
    assert j.get("status") == "ok"
