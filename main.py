import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

def read_csv_file(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

data = read_csv_file("filtered_stars.csv")

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()
