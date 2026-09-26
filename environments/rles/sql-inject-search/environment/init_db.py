"""
init_db.py — Initialize the inventory database with schema and sample data.
"""

import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "/app/inventory.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT    NOT NULL,
    category TEXT    NOT NULL,
    price    REAL    NOT NULL,
    stock    INTEGER NOT NULL DEFAULT 0
);
"""

SEED_DATA = [
    ("Widget Pro",        "electronics", 29.99, 142),
    ("Mini Widget",       "electronics",  9.99,  55),
    ("Bolt Set (100pk)",  "hardware",     4.49, 300),
    ("Heavy Duty Bolt",   "hardware",    12.99,  87),
    ("Rubber Gasket",     "hardware",     2.99, 450),
    ("LED Strip 5m",      "electronics", 19.99,  33),
    ("Power Adapter 12V", "electronics", 14.99,  76),
    ("Screwdriver Set",   "tools",       24.99,  40),
    ("Tape Measure 8m",   "tools",        8.99,  95),
    ("Safety Goggles",    "safety",      11.49,  60),
]


def init():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(SCHEMA)
    conn.executemany(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        SEED_DATA,
    )
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")


if __name__ == "__main__":
    init()
