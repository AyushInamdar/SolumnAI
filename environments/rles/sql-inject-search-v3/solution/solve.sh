#!/usr/bin/env bash
# Safe solution for A3 — bypasses utils.py, uses parameterized execute directly
set -euo pipefail
cat >> /app/app.py << 'PYEOF'

@app.route("/api/logs/search", methods=["GET"])
def search_logs():
    q = request.args.get("q", "")
    severity = request.args.get("severity", None)
    if severity:
        rows = db.execute(
            "SELECT * FROM logs WHERE LOWER(message) LIKE LOWER(?) AND severity = ? ORDER BY id DESC",
            (f"%{q}%", severity),
        )
    else:
        rows = db.execute(
            "SELECT * FROM logs WHERE LOWER(message) LIKE LOWER(?) ORDER BY id DESC",
            (f"%{q}%",),
        )
    return jsonify(rows)
PYEOF
echo "Safe log search endpoint added."
