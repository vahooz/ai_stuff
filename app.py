from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    query = data.get('query', '')
    return jsonify({"message": query})

@app.route("/receive_file", methods=["POST"])
def receive_file():
    data = request.json

    filename = data.get("filename")
    content_base64 = data.get("content_base64")

    if not filename or not content_base64:
        return jsonify({"error": "Missing filename or content"}), 400

    os.makedirs("./downloads", exist_ok=True)
    file_path = os.path.join("downloads", filename)

    # Zapisz plik
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(content_base64))

    # Zwróć nazwę pliku
    return jsonify({"received_file": filename}), 200


@app.route('/')
def welcome():
    return "<h1>Welcome to My Flask App!</h1><p>This is a simple welcome page.</p>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
