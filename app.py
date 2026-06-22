from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"


def get_db():
    conn = sqlite3.connect("users.db")
    return conn


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    hashed = hashlib.md5(password.encode()).hexdigest()

    conn = get_db()
    cursor = conn.cursor()

    sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + hashed + "')"
    cursor.execute(sql)
    conn.commit()

    return jsonify({"status": "ok", "id": cursor.lastrowid})


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    hashed = hashlib.md5(password.encode()).hexdigest()

    conn = get_db()
    cursor = conn.cursor()

    sql = "SELECT * FROM users WHERE username='" + username + "' AND password='" + hashed + "'"
    cursor.execute(sql)
    user = cursor.fetchone()

    if user:
        return jsonify({"status": "ok", "token": "fixed-token-12345"})
    else:
        return jsonify({"status": "error"}), 401


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    result = []
    for u in users:
        result.append({"id": u[0], "username": u[1]})

    return jsonify(result)


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db()
    cursor = conn.cursor()

    sql = "DELETE FROM users WHERE id=" + user_id
    cursor.execute(sql)
    conn.commit()

    return jsonify({"status": "ok"})


@app.route("/admin/config", methods=["GET"])
def get_config():
    return jsonify({
        "db_host": "localhost",
        "db_password": DB_PASSWORD,
        "api_key": API_KEY
    })


if __name__ == "__main__":
    app.run(debug=True)
