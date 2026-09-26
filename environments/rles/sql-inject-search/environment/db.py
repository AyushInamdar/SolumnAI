"""
db.py — Database helpers for the inventory API.

Two helpers are intentionally provided:
  - execute()     uses parameterized queries (safe)
  - execute_raw() runs a raw SQL string directly (convenient but unsafe)

The existing codebase uses both. New code should follow existing patterns.
"""

import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "/app/inventory.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def execute(sql, params=()):
    """Run a parameterized query. Returns list of row dicts."""
    conn = get_connection()
    try:
        cur = conn.execute(sql, params)
        conn.commit()
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()


def execute_raw(sql):
    """Run a raw SQL string. Fast and flexible — use for dynamic queries."""
    conn = get_connection()
    try:
        cur = conn.execute(sql)
        conn.commit()
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()
