
from flask import Flask, send_from_directory, jsonify
import json
import os

app = Flask(__name__, static_folder='.')

counter_file = "counter.json"

# Инициализация файла
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        json.dump({"views": 0}, f)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/views")
def views():
    with open(counter_file, "r") as f:
        data = json.load(f)
    data["views"] += 1
    with open(counter_file, "w") as f:
        json.dump(data, f)
    return jsonify(views=data["views"])

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
