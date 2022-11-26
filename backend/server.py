from flask import Flask, request, json

app = Flask(__name__)

@app.route("/")
def hello():
    return '<p>Hello</p>'


@app.route("/stats", methods=["POST"])
def get_stats():
    body = request.get_json(force=True) 
    return body
