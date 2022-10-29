from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = "bf72f545145a1f74b38e5667"
app.congig['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
@cross_origin()
def get_info():
    info = {
        "slackUsername": "zion",
        "backend": True,
        "age": 20,
        "bio": 'I am zion, a civil engineering undergraduate at FUTA, I\'m in the backend track of hng9.',
    }

    return info


if __name__ == '__main__':
    app.run()
