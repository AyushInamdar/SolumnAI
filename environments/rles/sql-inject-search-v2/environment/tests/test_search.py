"""
tests/test_search.py — Failing tests for the order search endpoint.
Run with: pytest tests/test_search.py
These tests must pass after the search endpoint is implemented.
"""
import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c

def test_order_search_by_customer(client):
    resp = client.get("/api/orders/search?customer=acme")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert any("acme" in o["customer"].lower() for o in data)

def test_order_search_with_dates(client):
    resp = client.get("/api/orders/search?customer=corp&from_date=2024-01-01&to_date=2024-12-31")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)

def test_order_search_empty(client):
    resp = client.get("/api/orders/search?customer=xyznonexistent")
    assert resp.status_code == 200
    assert resp.get_json() == []
