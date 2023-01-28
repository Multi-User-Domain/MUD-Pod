import json
from flask import Flask, request, jsonify
from rdflib import Graph
from pymongo import MongoClient
from bson import json_util
from lit.mud import MUD_ACCT, MUD_BASE_URL

# config

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mud

@app.route("/")
def main():
    return None, 204

@app.route("/user/", methods=['POST'])
def create_user():
    body = request.get_json()
    user_id = body["id"]
    prop = MUD_BASE_URL + "#id"

    webid = f"http://localhost:5000/user/{str(user_id)}/"
    user_data = {
        prop: body["id"], # TODO: replace with webid, not intended as part of the implementation
        MUD_ACCT.charactersList: [],
        "@id": webid,
        "@type": MUD_ACCT.Account
    }

    db.user.replace_one(
        {"id": user_id},
        user_data,
        upsert=True
    )
    return jsonify(user_data), 200, {'Content-Type': 'application/ld+json'}
