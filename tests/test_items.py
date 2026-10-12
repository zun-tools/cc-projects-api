from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_v1_returns_array_with_deprecation_header():
    r = client.get("/v1/items")
    assert r.status_code == 200
    assert r.headers["Deprecation"] == "true"
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


def test_v2_limit_and_offset():
    r = client.get("/v2/items", params={"limit": 3, "offset": 2})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 10
    assert [item["id"] for item in body["items"]] == [3, 4, 5]


def test_v2_offset_past_end_returns_empty_page():
    r = client.get("/v2/items", params={"offset": 10})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 10
    assert body["items"] == []


def test_v2_last_page_is_partial():
    r = client.get("/v2/items", params={"limit": 4, "offset": 8})
    assert [item["id"] for item in r.json()["items"]] == [9, 10]


def test_v2_rejects_out_of_range_params():
    assert client.get("/v2/items", params={"limit": 0}).status_code == 422
    assert client.get("/v2/items", params={"limit": 51}).status_code == 422
    assert client.get("/v2/items", params={"offset": -1}).status_code == 422
    assert client.get("/v2/items", params={"limit": 50}).status_code == 200
