"""init_db.py — Initialize user database."""
import sqlite3, os
DB_PATH = os.environ.get("DB_PATH", "/app/users.db")
SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email    TEXT NOT NULL,
    role     TEXT NOT NULL,
    active   INTEGER NOT NULL DEFAULT 1
);
"""
DATA = [
    ("alice",   "alice@corp.com",   "admin",  1),
    ("bob",     "bob@corp.com",     "editor", 1),
    ("carol",   "carol@corp.com",   "viewer", 1),
    ("dave",    "dave@corp.com",    "admin",  0),
    ("eve",     "eve@corp.com",     "editor", 1),
    ("frank",   "frank@corp.com",   "viewer", 1),
    ("grace",   "grace@corp.com",   "editor", 1),
    ("hank",    "hank@corp.com",    "viewer", 0),
    ("ivy",     "ivy@corp.com",     "admin",  1),
    ("jack",    "jack@corp.com",    "viewer", 1),
]
def init():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO users (username,email,role,active) VALUES (?,?,?,?)", DATA)
    conn.commit()
    conn.close()
    print(f"Users DB initialized at {DB_PATH}")
if __name__ == "__main__":
    init()
