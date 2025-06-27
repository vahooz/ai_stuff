from flask import Flask, request, jsonify, send_file, Response
import base64
import os, io
import json

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    query = data.get('query', '')
    return jsonify({"message": query})


@app.route("/upload", methods=["POST"])
def upload_file():
    print("HEADERS:", dict(request.headers))
    print("RAW DATA:", request.get_data())

    content_type = request.headers.get('Content-Type')
    if content_type != 'application/octet-stream':
        return "Unsupported Media Type", 415

    # Pobierz nazwę pliku z nagłówka
    content_disp = request.headers.get('Content-Disposition', 'attachment; filename=uploaded_file')
    filename = content_disp.split("filename=")[-1].strip('"')

    # Przeczytaj zawartość
    file_content = request.get_data()

    new_filename = f"renamed_{filename}"

    # Utwórz obiekt in-memory i zwróć go jako odpowiedź
    return send_file(
        io.BytesIO(file_content),
        mimetype='application/octet-stream',
        as_attachment=True,
        download_name=new_filename  # Flask 2.x+
    )


@app.route("/encoded_upload", methods=["POST"])
def upload_file_base64():
    print("DATA:", dict(request.data))    
    data = json.loads(request.data)
    content = base64.b64decode(data["content"])
    return Response(content, mimetype="text/plain")


@app.route('/')
def welcome():
    return "<h1>Welcome to My Flask App!</h1><p>This is a simple welcome page.</p>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
