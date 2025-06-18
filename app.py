from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    query = data.get('query', '')
    return jsonify({"message": query})

@app.route('/')
def welcome():
    return "<h1>Welcome to My Flask App!</h1><p>This is a simple welcome page.</p>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
