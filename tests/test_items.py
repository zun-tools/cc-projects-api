from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_v1_returns_array_with_deprecation_header():
    r = client.get("/v1/items")
    assert r.status_code == 200
    assert r.headers["Deprecation"] == "true"
    assert r.headers["Link"] == '</v2/items>; rel="successor-version"'
    body = r.json()
    assert isinstance(body, list)
    assert len(body) == 10


def test_v2_returns_items_and_total():
    r = client.get("/v2/items")
    assert r.status_code == 200
    assert "Deprecation" not in r.headers
    body = r.json()
    assert body["total"] == 10
    assert len(body["items"]) == 10
    assert body["items"][0] == {"id": 1, "name": "りんご", "price": 120}
