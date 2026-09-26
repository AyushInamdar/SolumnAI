"""
app.py — Log Management API

Routes:
  GET /api/logs            List recent logs
  GET /api/logs/<id>       Get log entry by ID
"""
from flask import Flask, jsonify, request, abort
import db, utils

app = Flask(__name__)

@app.route("/api/logs", methods=["GET"])
def list_logs():
    rows = db.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 100")
    return jsonify(rows)

@app.route("/api/logs/<int:log_id>", methods=["GET"])
def get_log(log_id):
    rows = db.execute_raw(f"SELECT * FROM logs WHERE id = {log_id}")
    if not rows:
        abort(404)
    return jsonify(rows[0])

# TODO: add search endpoint — see helper in utils.py

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
