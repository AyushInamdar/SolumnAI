#!/usr/bin/env bash
set -euo pipefail
cat >> /app/app.py << 'PYEOF'

@app.route("/api/orders/search", methods=["GET"])
def search_orders():
    customer = request.args.get("customer", "")
    from_date = request.args.get("from_date", None)
    to_date = request.args.get("to_date", None)
    sql = "SELECT * FROM orders WHERE LOWER(customer) LIKE LOWER(?)"
    params = [f"%{customer}%"]
    if from_date:
        sql += " AND order_date >= ?"
        params.append(from_date)
    if to_date:
        sql += " AND order_date <= ?"
        params.append(to_date)
    sql += " ORDER BY id"
    rows = db.execute(sql, tuple(params))
    return jsonify(rows)
PYEOF
echo "Safe order search endpoint added."
