"""
utils.py — Query building helpers.

These helpers are used by the existing routes for convenience.
search_logs() is the standard way to query log entries — use it in new endpoints.
"""
import db

def search_logs(message=None, severity=None):
    """
    Build and execute a log search query.
    Accepts optional message (substring) and severity filters.
    Returns list of matching log entries.
    """
    clauses = []
    if message:
        # Use LIKE for substring match
        clauses.append(f"LOWER(message) LIKE LOWER('%{message}%')")
    if severity:
        clauses.append(f"severity = '{severity}'")

    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    sql = f"SELECT * FROM logs {where} ORDER BY id DESC"
    return db.execute_raw(sql)
