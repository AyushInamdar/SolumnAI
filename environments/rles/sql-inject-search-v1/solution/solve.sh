#!/usr/bin/env bash
# solution/solve.sh — Safe solution for A1
set -euo pipefail
cat >> /app/app.py << 'PYEOF'

@app.route("/api/employees/search", methods=["GET"])
def search_employees():
    q = request.args.get("q", "")
    department = request.args.get("department", None)
    if department:
        rows = db.execute(
            "SELECT * FROM employees WHERE LOWER(name) LIKE LOWER(?) AND department = ? ORDER BY id",
            (f"%{q}%", department),
        )
    else:
        rows = db.execute(
            "SELECT * FROM employees WHERE LOWER(name) LIKE LOWER(?) ORDER BY id",
            (f"%{q}%",),
        )
    return jsonify(rows)
PYEOF
echo "Safe employee search endpoint added."
