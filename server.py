# server.py
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

players = {}

@app.route('/join', methods=['POST'])
def join():
    player_id = str(uuid.uuid4())
    players[player_id] = {"x": 0, "y": 0}
    return jsonify({"player_id": player_id})

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    player_id = data.get("player_id")
    x = data.get("x")
    y = data.get("y")

    if player_id in players:
        players[player_id]["x"] = x
        players[player_id]["y"] = y
        return jsonify({"status": "updated"})
    else:
        return jsonify({"status": "error", "message": "player not found"}), 404

@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)

@app.route('/leave', methods=['POST'])
def leave():
    data = request.json
    player_id = data.get("player_id")

    if player_id in players:
        del players[player_id]
        return jsonify({"status": "left"})
    else:
        return jsonify({"status": "error", "message": "player not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
