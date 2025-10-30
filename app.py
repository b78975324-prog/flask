from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with a few entries
DATA = [
    {"name": "Alice",   "email": "alice@example.com"},
    {"name": "Bob",     "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

@app.route("/get", methods=["GET"])
def get_entry():
    return jsonify(DATA)


@app.route("/post", methods=["POST"])
def post_entry():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    entry = {"name": name, "email": email}
    DATA.append(entry)
    return jsonify(DATA)


@app.route("/delete/<int:Index>", methods=["DELETE"])
def delete_entry(Index):
    DATA.pop(Index)
    return jsonify(DATA)



@app.route("/update/<int:Index>", methods=["PUT"])
def update_entry(Index):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    DATA[Index] = {"name": name, "email": email}
    return jsonify(DATA)


if __name__ == "__main__":
    app.run()  # http://127.0.0.1:5000
