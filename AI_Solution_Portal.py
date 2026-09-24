# AI-Solution-Portal

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "AI Solution Portal",
        "status": "Running",
        "message": "AI Solution Portal Backend Started"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status" : "success",
        "message": "Backend is working"
    })

if __name__ == "__name__":
    app.run(debug=True)
