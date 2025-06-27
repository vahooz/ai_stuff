from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    query = data.get('query', '')
    return jsonify({"message": query})

@app.route("/upload", methods=["POST"])
def upload_file():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/octet-stream':
        return "Unsupported Media Type", 415

    filename = request.headers.get('Content-Disposition', 'attachment; filename=uploaded_file').split("filename=")[-1].strip('"')
    file_content = request.get_data()

    with open(f"./uploads/{filename}", "wb") as f:
        f.write(file_content)

    return f"Plik {filename} zapisany", 200


@app.route('/')
def welcome():
    return "<h1>Welcome to My Flask App!</h1><p>This is a simple welcome page.</p>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
