from flask import Flask, render_template, request
from brain import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("userMessage")
    return get_response(user_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)