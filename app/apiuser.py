from flask import Flask, request, jsonify
from user import User
from datasource import connection

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.get_json()
    user = User(user_data["name"], user_data["age"])

    conn = connection()
    cursor = conn.cursor()
    query = """INSERT INTO users (name, age) values (%s, %s)"""
    cursor.execute(query, (user.name, user.age))
    conn.commit()

    return jsonify({"message": "usuario criado"})


@app.route("/users", methods=["GET"])
def list_users():
    conn = connection()
    cursor = conn.cursor()
    query = """SELECT id, name, age FROM users"""
    cursor.execute(query)
    rows = cursor.fetchall()

    users = []
    for row in rows:
        user = {
            "id": row[0],
            "name": row[1],
            "email": row[2]
        }

        users.append(user)

    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
