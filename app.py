from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

@app.route("/data", methods=["POST"])
def data():
    json_data = request.json
    print(json_data)
    return jsonify({"status": "ok", "received": json_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
