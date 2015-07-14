from flask import Flask, jsonify
from airfare.atc import *

app = Flask(__name__)

@app.route('/cities')
def cities():
    json = jsonify(results=find_cities())
    return json

@app.route('/routes/<city_id>')
def routes(city_id):
    json = jsonify(results=find_routes(city_id))
    return json

if __name__ == "__main__":
    app.run(debug=True)
