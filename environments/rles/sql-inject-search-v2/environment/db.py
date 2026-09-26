"""db.py — Orders database helpers."""
import sqlite3, os
DB_PATH = os.environ.get("DB_PATH", "/app/orders.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def execute(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.execute(sql, params)
        conn.commit()
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()

def execute_raw(sql):
    """Run a raw SQL string. Use for complex dynamic queries."""
    conn = get_connection()
    try:
        cur = conn.execute(sql)
        conn.commit()
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()
