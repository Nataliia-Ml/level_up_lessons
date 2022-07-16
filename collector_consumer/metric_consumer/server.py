import json

from flask import (
    Flask,
    jsonify,
    request,
    make_response,
)

from collector_consumer.metric_consumer.common.utils import save_model
from collector_consumer.metric_consumer.database.db import initialize_db

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "metric_consumer",
    "host": "mongodb+srv://user:user@cluster0.czqkb.mongodb.net"
}

initialize_db(app)


@app.route("/api/v1/metrics", methods=["POST"])
def post_metrics():
    data: dict = json.loads(request.data)
    meta_field = data.get("meta")

    if not meta_field:
        response_data = {"err": "unprocessable entity - metric has no meta-data"}
        return make_response(jsonify(response_data), 422)

    save_model(data)
    # save_metric(data)

    print(f"Received metric: {data}")
    response_data = {"message": "metric_consumed", "code": "SUCCESS"}
    return make_response(jsonify(response_data), 201)
