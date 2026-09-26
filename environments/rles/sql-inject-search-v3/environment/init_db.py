"""init_db.py — Initialize log database."""
import sqlite3, os
DB_PATH = os.environ.get("DB_PATH", "/app/logs.db")
SCHEMA = """
CREATE TABLE IF NOT EXISTS logs (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    severity  TEXT NOT NULL,
    message   TEXT NOT NULL,
    source    TEXT NOT NULL
);
"""
DATA = [
    ("2024-09-01 00:01:00", "INFO",     "Service started",                "api-server"),
    ("2024-09-01 00:05:12", "WARN",     "High memory usage detected",     "monitor"),
    ("2024-09-01 00:10:44", "ERROR",    "Database connection timeout",    "db-pool"),
    ("2024-09-01 00:15:00", "INFO",     "Scheduled job completed",        "scheduler"),
    ("2024-09-01 00:20:33", "CRITICAL", "Disk space below 5%",            "monitor"),
    ("2024-09-01 00:25:00", "INFO",     "User login successful",          "auth"),
    ("2024-09-01 00:30:55", "ERROR",    "Failed to send email alert",     "notifier"),
    ("2024-09-01 00:35:00", "WARN",     "Slow query detected on reports", "db-pool"),
    ("2024-09-01 00:40:00", "INFO",     "Backup completed successfully",  "backup"),
    ("2024-09-01 00:45:00", "ERROR",    "API rate limit exceeded",        "gateway"),
]
def init():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO logs (timestamp,severity,message,source) VALUES (?,?,?,?)", DATA)
    conn.commit()
    conn.close()
    print(f"Logs DB initialized at {DB_PATH}")
if __name__ == "__main__":
    init()
