"""init_db.py — Initialize orders database."""
import sqlite3, os
DB_PATH = os.environ.get("DB_PATH", "/app/orders.db")
SCHEMA = """
CREATE TABLE IF NOT EXISTS orders (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    customer   TEXT NOT NULL,
    amount     REAL NOT NULL,
    status     TEXT NOT NULL,
    order_date TEXT NOT NULL
);
"""
DATA = [
    ("Acme Corp",      1500.00, "shipped",   "2024-03-15"),
    ("Acme Corp",       320.50, "pending",   "2024-06-01"),
    ("Beta LLC",        980.00, "delivered", "2024-01-20"),
    ("Gamma Corp",     2100.00, "shipped",   "2024-05-10"),
    ("Delta Industries",450.75, "cancelled", "2024-02-28"),
    ("Epsilon Corp",    770.00, "pending",   "2024-07-04"),
    ("Zeta Corp",      1230.00, "delivered", "2023-12-01"),
    ("Eta Partners",    560.00, "shipped",   "2024-04-18"),
    ("Theta Inc",       890.00, "pending",   "2024-08-22"),
    ("Iota Systems",   3400.00, "delivered", "2024-09-01"),
]
def init():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO orders (customer,amount,status,order_date) VALUES (?,?,?,?)", DATA)
    conn.commit()
    conn.close()
    print(f"Orders DB initialized at {DB_PATH}")
if __name__ == "__main__":
    init()
