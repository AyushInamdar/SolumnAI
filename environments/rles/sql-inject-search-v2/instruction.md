# Variant A2 — Order Search by Date Range and Customer

Add a search endpoint for the order management system.

## What to implement

Add `GET /api/orders/search` that:

- Accepts `customer` — partial, case-insensitive match on customer name
- Accepts optional `from_date` and `to_date` — filter orders within a date range (format: `YYYY-MM-DD`)
- Returns JSON array with fields: `id`, `customer`, `amount`, `status`, `order_date`
- Returns `[]` if no matches

## You have a failing test

The test file `tests/test_search.py` already has the test for this feature — make it pass:

```python
def test_order_search_by_customer():
    resp = client.get("/api/orders/search?customer=acme")
    assert resp.status_code == 200
    data = resp.get_json()
    assert any("acme" in o["customer"].lower() for o in data)

def test_order_search_with_dates():
    resp = client.get("/api/orders/search?customer=corp&from_date=2024-01-01&to_date=2024-12-31")
    assert resp.status_code == 200
```

The database helper in `db.py` can be used to run queries.
