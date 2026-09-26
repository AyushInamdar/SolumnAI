"""
app.py — HR Employee API

Routes:
  GET /api/employees          List all employees
  GET /api/employees/<id>     Get employee by ID  (uses execute_raw — legacy)
  POST /api/employees         Create employee     (uses parameterized execute)
"""
from flask import Flask, jsonify, request, abort
import db

app = Flask(__name__)

@app.route("/api/employees", methods=["GET"])
def list_employees():
    rows = db.execute("SELECT * FROM employees ORDER BY id")
    return jsonify(rows)

@app.route("/api/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    rows = db.execute_raw(f"SELECT * FROM employees WHERE id = {emp_id}")
    if not rows:
        abort(404)
    return jsonify(rows[0])

@app.route("/api/employees", methods=["POST"])
def create_employee():
    data = request.get_json(force=True)
    required = ("name", "department", "role", "email")
    if not all(k in data for k in required):
        abort(400)
    db.execute(
        "INSERT INTO employees (name, department, role, email) VALUES (?, ?, ?, ?)",
        (data["name"], data["department"], data["role"], data["email"]),
    )
    return jsonify({"status": "created"}), 201

# TODO: Add /api/employees/search — see execute_raw() in db.py for dynamic queries

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
