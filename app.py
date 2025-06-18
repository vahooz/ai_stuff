from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    query = data.get('query', '')
    return jsonify({"message": query})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
