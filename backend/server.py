from flask import Flask, request
from database import Database
from stats import generate_json

app = Flask(__name__)
db = Database()

@app.route("/")
def hello():
    return '<p>Hello</p>'


@app.route("/stats", methods=["POST"])
def get_stats():
    body = request.get_json(force=True)
    collection = list(db.get_collection(body))
    
    if not collection:
        return {}
    collection = collection[0]
    data = collection['data']
    names = collection['columns']
    ready_json = generate_json(data, names)
    print(ready_json)
    return ready_json
