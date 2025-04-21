# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Pygame Flask Server is Running!"

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    print(f"Player moved to: {data}")
    return jsonify({"status": "received", "position": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
