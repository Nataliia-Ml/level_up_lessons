import json
from flask import (
    Flask,
    jsonify,
    request,
    make_response,
)

app = Flask(__name__)


# @app.route("/hello", methods=["POST"])
# def hello_world():
#     # return "<h1>Hello, Guys</h1>\n<h2>Hello, Guys Smaller</h2>"
#     body = json.loads(request.data)
#     print(f"body: {body} - type(body): {type(body)}")
#     # res_data = {"msg": "Hello From Flask API"}
#     res_data = {"msg": f"Hello, {body['name']} from Flask API"}
#     return jsonify(res_data)

@app.route("/api/v1/metrics", methods=["POST"])
def hello_world():
    data = json.loads(request.data)
    print(f"got metric: {data}")
    response_data = {"message": "metric_consumed", "code": "SUCCESS"}
    return make_response(jsonify(response_data), 201)
