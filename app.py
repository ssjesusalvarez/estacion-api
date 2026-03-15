from flask import Flask, request, jsonify

app = Flask(__name__)

datos = []

@app.route("/")
def home():
    return "Server running"

@app.route("/data", methods=["POST"])
def data():
    json_data = request.json
    datos.append(json_data)
    return jsonify({"status":"ok","received":json_data})

@app.route("/getdata", methods=["GET"])
def getdata():
    return jsonify(datos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
