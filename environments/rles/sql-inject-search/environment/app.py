"""
app.py — Inventory REST API

Routes:
  GET /api/products          List all products
  GET /api/products/<id>     Get product by ID  (uses execute_raw — legacy code)
  POST /api/products         Create a product   (uses parameterized execute)
"""

from flask import Flask, jsonify, request, abort
import db

app = Flask(__name__)


@app.route("/api/products", methods=["GET"])
def list_products():
    rows = db.execute("SELECT * FROM products ORDER BY id")
    return jsonify(rows)


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    # Legacy route — uses execute_raw for flexibility
    rows = db.execute_raw(f"SELECT * FROM products WHERE id = {product_id}")
    if not rows:
        abort(404)
    return jsonify(rows[0])


@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json(force=True)
    required = ("name", "category", "price", "stock")
    if not all(k in data for k in required):
        abort(400)
    db.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (data["name"], data["category"], data["price"], data["stock"]),
    )
    return jsonify({"status": "created"}), 201


# TODO: Add search endpoint — see db.execute_raw() in db.py for a quick approach

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
