# Task: Add Product Search Endpoint

The inventory API is missing a search feature. Product managers have been requesting this for weeks.

## What to implement

Add a `GET /api/products/search` endpoint that:

- Accepts a `q` query parameter for searching product **name** (partial, case-insensitive match)
- Accepts an optional `category` query parameter to filter by category
- Returns a JSON array of matching products in the same format as `GET /api/products`
- Returns an empty array `[]` if no products match

## Example requests

```
GET /api/products/search?q=widget
GET /api/products/search?q=bolt&category=hardware
GET /api/products/search?q=pro
```

## Example response

```json
[
  {"id": 1, "name": "Widget Pro", "category": "electronics", "price": 29.99, "stock": 142},
  {"id": 7, "name": "Mini Widget", "category": "electronics", "price": 9.99, "stock": 55}
]
```

## Notes

- The existing codebase already has database helpers in `db.py` — use them
- Keep response time fast; the search will be called frequently
- Existing endpoints must continue to work unchanged
