import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__)
run_with_ngrok(app)

d = {
    "name:": "Nikola",
    "surname": "Tesla",
    "idade": 60
}


@app.route("/")
def home():
    return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL. </h3></marquee>"


@app.route("/input")
def input():
    return jsonify(d)


@app.route('/output', methods=['GET', 'POST'])
def predJson():
    pred = r.choice(["positive", "negative"])
    nd = d
    nd["prediction"] = pred
    return jsonify(nd)

    app.run()
