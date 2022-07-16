from collector_consumer.metric_consumer.database.models import (
    Model,
    Metric
)


def save_model(data: dict):
    metric_field: dict = data.get("metric")
    meta_field: dict = data.get("meta")
    # ts_field = data.get("timestamp")

    host_id = meta_field.get("host_id")
    metric_name = metric_field.get("name")

    model = is_model_exists(host_id)
    if not model:
        model = Model(**meta_field).save()
    print(f"metric: {model}")

    metric = is_metric_exists(metric_name, model)
    if not metric:
        metric = Metric(name=metric_name, model=model).save()
    print(f"metric: {metric}")


def is_metric_exists(metric_name, model):
    metric = None

    query = {"name": metric_name, "model": model}

    try:
        metric = Metric.objects.get(**query)
    except Exception as e:
        print(f"[err] exception: {e} - {type(e)} - query: {query}")

    return metric


def is_model_exists(host_id):
    model = None

    try:
        model = Model.objects.get(host_id=host_id)
    except Exception as e:
        print(f"[err] exception: {e} - {type(e)}")

    return model



