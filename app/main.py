from fastapi import FastAPI, Response

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
    response.headers["Link"] = '</v2/items>; rel="successor-version"'
    return ITEMS


@app.get("/v2/items")
def list_items_v2():
    """Returns an object with items and total. No pagination yet."""
    return {"items": ITEMS, "total": len(ITEMS)}
