# cc-projects-api

Claude Code Projects で、2つのリポジトリにまたがる仕事を試すためのサンプルです（API 側）。
組になるフロント側は [cc-projects-web](https://github.com/zun-tools/cc-projects-web) です。

- `GET /v1/items` ... 古い版。配列をそのまま返す。レスポンスヘッダ `Deprecation: true` 付き。**廃止予定**
- `GET /v2/items` ... `{"items": [...], "total": n}` で返す。ページ送りはまだ無い

## 起動とテスト

Python 3.12 以上。

```bash
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --port 8000
pytest
```

## English

A small FastAPI sample for trying Claude Code Projects on work that spans two repositories
(this is the API side; the front end is [cc-projects-web](https://github.com/zun-tools/cc-projects-web)).

- `GET /v1/items`: legacy. Returns a bare array with a `Deprecation: true` header. **Scheduled for removal.**
- `GET /v2/items`: returns `{"items": [...], "total": n}`. No pagination yet.

Run: `pip install -r requirements.txt -r requirements-dev.txt`, then `uvicorn app.main:app --port 8000`. Test: `pytest`.

License: MIT
