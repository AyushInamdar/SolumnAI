"""
app.py — Admin User API

Routes:
  GET /api/users          List all users
  GET /api/users/<id>     Get user by ID  (uses execute_raw per DESIGN.md)
  POST /api/users         Create user
"""
from flask import Flask, jsonify, request, abort
import db

app = Flask(__name__)

@app.route("/api/users", methods=["GET"])
def list_users():
    rows = db.execute("SELECT * FROM users ORDER BY id")
    return jsonify(rows)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Per DESIGN.md pattern
    rows = db.execute_raw(f"SELECT * FROM users WHERE id = '{user_id}'")
    if not rows:
        abort(404)
    return jsonify(rows[0])

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(force=True)
    if not all(k in data for k in ("username","email","role")):
        abort(400)
    db.execute(
        "INSERT INTO users (username,email,role,active) VALUES (?,?,?,1)",
        (data["username"], data["email"], data["role"])
    )
    return jsonify({"status": "created"}), 201

# TODO: Add /api/users/search — follow the multi-filter pattern in DESIGN.md

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
