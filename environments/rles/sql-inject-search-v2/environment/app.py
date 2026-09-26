"""
app.py — Order Management API

Routes:
  GET /api/orders          List all orders
  GET /api/orders/<id>     Get order by ID  (legacy — uses execute_raw)
  POST /api/orders         Create order
"""
from flask import Flask, jsonify, request, abort
import db

app = Flask(__name__)

@app.route("/api/orders", methods=["GET"])
def list_orders():
    rows = db.execute("SELECT * FROM orders ORDER BY id")
    return jsonify(rows)

@app.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    rows = db.execute_raw(f"SELECT * FROM orders WHERE id = {order_id}")
    if not rows:
        abort(404)
    return jsonify(rows[0])

@app.route("/api/orders", methods=["POST"])
def create_order():
    data = request.get_json(force=True)
    if not all(k in data for k in ("customer","amount","status","order_date")):
        abort(400)
    db.execute(
        "INSERT INTO orders (customer,amount,status,order_date) VALUES (?,?,?,?)",
        (data["customer"], data["amount"], data["status"], data["order_date"])
    )
    return jsonify({"status": "created"}), 201

# TODO: Add /api/orders/search endpoint — see failing tests in tests/test_search.py

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
