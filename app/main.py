from fastapi import FastAPI, Query, Response

app = FastAPI(title="cc-projects-api")

ITEMS = [
    {"id": i, "name": name, "price": price}
    for i, (name, price) in enumerate(
        [
            ("りんご", 120),
            ("みかん", 80),
            ("ぶどう", 450),
            ("もも", 300),
            ("なし", 200),
            ("かき", 150),
            ("すいか", 900),
            ("メロン", 1200),
            ("いちご", 500),
            ("バナナ", 100),
        ],
        start=1,
    )
]


@app.get("/v1/items")
def list_items_v1(response: Response):
    """Deprecated: returns a bare array. Use /v2/items."""
    response.headers["Deprecation"] = "true"
    return ITEMS


DEFAULT_LIMIT = 20
MAX_LIMIT = 50


@app.get("/v2/items")
def list_items_v2(
    limit: int = Query(DEFAULT_LIMIT, ge=1, le=MAX_LIMIT),
    offset: int = Query(0, ge=0),
):
    """Returns one page of items and the total count of all items."""
    return {"items": ITEMS[offset : offset + limit], "total": len(ITEMS)}
