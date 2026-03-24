from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data (temporary database)
users = [
    {"id": 1, "name": "Nilesh"},
    {"id": 2, "name": "Rahul"}
]

# Home route
@app.route('/')
def home():
    return "Flask API is working!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"})

    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)