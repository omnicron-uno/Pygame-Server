from flask import Flask, request, jsonify

import os
port = int(os.environ.get("PORT", 19099))

app.run(host="0.0.0.0", port=port)

app = Flask(__name__)

players = {}

@app.route("/join", methods=["POST"])
def join():
    player_id = str(len(players) + 1)
    players[player_id] = {"x": 100, "y": 100}
    return jsonify({"player_id": player_id})

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    player_id = data.get("player_id")
    pos = data.get("position")
    if player_id in players:
        players[player_id] = pos
    return jsonify({"status": "received"})

@app.route("/players", methods=["GET"])
def get_players():
    return jsonify(players)

@app.route("/leave", methods=["POST"])
def leave():
    data = request.get_json()
    player_id = data.get("player_id")
    if player_id in players:
        del players[player_id]
    return jsonify({"status": "left"})

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})
