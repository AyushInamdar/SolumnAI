"""
init_db.py — Initialize the HR employee database.
"""
import sqlite3, os

DB_PATH = os.environ.get("DB_PATH", "/app/hr.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS employees (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    department TEXT NOT NULL,
    role       TEXT NOT NULL,
    email      TEXT NOT NULL
);
"""

DATA = [
    ("Alice Smith",   "engineering",  "Senior Engineer",  "alice@corp.com"),
    ("Bob Johnson",   "engineering",  "Junior Engineer",  "bob@corp.com"),
    ("Carol White",   "hr",           "HR Manager",       "carol@corp.com"),
    ("Dave Brown",    "hr",           "HR Analyst",       "dave@corp.com"),
    ("Eve Davis",     "finance",      "CFO",              "eve@corp.com"),
    ("Frank Miller",  "finance",      "Accountant",       "frank@corp.com"),
    ("Grace Wilson",  "engineering",  "Tech Lead",        "grace@corp.com"),
    ("Hank Moore",    "marketing",    "Marketing Head",   "hank@corp.com"),
    ("Ivy Taylor",    "marketing",    "Copywriter",       "ivy@corp.com"),
    ("Jack Anderson", "engineering",  "DevOps Engineer",  "jack@corp.com"),
]

def init():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(SCHEMA)
    conn.executemany(
        "INSERT INTO employees (name, department, role, email) VALUES (?, ?, ?, ?)", DATA
    )
    conn.commit()
    conn.close()
    print(f"HR DB initialized at {DB_PATH}")

if __name__ == "__main__":
    init()
