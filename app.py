import uuid

from flask import Flask, jsonify, request

# init Flask app
app = Flask(__name__)

_cars = []

@app.route("/cars/add", methods= ['POST'])
def add_one_car():
    car = request.get_json()
    car["id"] = str( uuid.uuid4() )

    _cars.append(car)

    return jsonify(status= 'success', num_cars = len(_cars))


# @app.route("/cars/add/<car>", methods= ['GET'])
# def add_car(id):
#     x = id
#
#     car = {
#         "year": 1979,
#         "make": "cheyy",
#         "model": "pinto",
#         "owner_id": 1
#     }
#     car["id"] = str(uuid.uuid4())
#     _cars.append(car)
#     return _cars
    # spec = {"name": "car_server"}
    # return jsonify(spec)

@app.route("/cars", methods= ['GET'])
def get_cars():
    return _cars
    # spec = {"name": "car_server"}
    # return jsonify(spec)

@app.route("/")
def home():
    data = {"name": "car_server"}
    return jsonify(data)


if __name__ == "__main__":
    app.run( host='0.0.0.0', debug=True )