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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
