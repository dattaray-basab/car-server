import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# init Flask app
app = Flask(__name__)
CORS(app)

_cars = []

@app.route("/cars", methods= ['POST'])
def add_one_car():
    car = request.get_json()
    car["id"] = str( uuid.uuid4() )

    _cars.append(car)

    return jsonify(status= 'success', num_cars = len(_cars))


@app.route("/cars", methods= ['GET'])
def get_cars():
    return _cars

@app.route("/")
def home():
    data = {"name": "car_server"}
    return jsonify(data)


if __name__ == "__main__":
    app.run( host='0.0.0.0', debug=True )