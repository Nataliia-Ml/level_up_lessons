from ..database.db import db


class Units(db.Document):
    name = db.StringField(required=True, unique=True)


class Model(db.Document):
    source_name = db.StringField(required=True, unique=False)
    hostname = db.StringField(required=True, unique=False)
    host_id = db.StringField(required=True, unique=True)

    meta = {"collection": "models"}


class Metric(db.Document):
    name = db.StringField(required=True, unique=False)
    # values = db.ListField("MetricValues", default=list)
    # units = db.ReferenceField("Units")
    model = db.ReferenceField("Model")

    meta = {"collection": "metrics"}


class MetricValues(db.Document):
    ts = db.DateTimeField()
    value = db.FloatField()

    meta = {"collection": "metric_values"}


