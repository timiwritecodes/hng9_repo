from flask import Flask, jsonify, request
from flask_cors import cross_origin
from enum import Enum


app = Flask(__name__)
app.config['SECRET_KEY'] = "bf72f545145a1f74b38e5667"
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
@cross_origin()
def get_info():
    info = {
        "slackUsername": "zion01",
        "backend": True,
        "age": 20,
        "bio": 'I am zion, a civil engineering undergraduate at FUTA, I\'m in the backend track of hng9.',
    }

    return jsonify(info)


@app.route('/operations', methods=['POST'])
@cross_origin()
def evaluate_integer():
    request_data = request.get_json()

    slackUsername = "zion01"
    x = None
    y = None

    result = None
    op = request.json['operation_type']
    print(type(op))
    print(op)
    if request_data:
        if 'x' in request_data:
            x = request_data['x']
        if 'y' in request_data:
            y = request_data['y']

    class Calc(Enum):
        ADD = "addition"
        SUB = "subtraction"
        MULT = "multiplication"

    operations = [item.value for item in Calc]

    operations_dict = {'addition': x+y, 'multiplication': x*y, 'subtraction': x-y}

    if request_data:
        if 'operation_type' in request_data:
            if op in operations:
                result = operations_dict[op]
            else:
                return {
                    "message": "your operator_type should be 'add', 'subtract', 'multiply'"
                        }
        else:
            return {
                "message": "operation_type field is empty"
            }

    return {
            "slackUsername": slackUsername,
            "result": result,
            "operation_type": op
                }


if __name__ == '__main__':
    app.run()
