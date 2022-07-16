from time import time
from typing import List

import psutil

from config import AgentConfig
from metric import Metric, MetricModel


class AgentCollector(AgentConfig):

    metric_keys = ("name", "value", "units")

    def __init__(self, *args, **kwargs):
        self.metrics_models: List[MetricModel] = [] # в этот пустой спислк будут записаны Metric_Model
        super().__init__(*args, **kwargs)

    def collect_cpu_metrics(self):
        """
        descr: represents the CPU time has spent in the given mode (user/system/idle)
        units: seconds
        :return: None
        """

        if not self.cpu:
            return False

        units = "seconds"
        cpu_metrics = psutil.cpu_times()

        data = [
            ("cpu_time_user", cpu_metrics.user, units),
            ("cpu_time_system", cpu_metrics.system, units),
            ("cpu_time_idle", cpu_metrics.idle, units),
        ]

        self.save_metrics(data)

    def collect_memory_metrics(self):
        """
        descr: Return statistics about system memory usage
        units: bytes
        :return: None
        """

        if not self.memory:
            return False

        units = "bytes"
        virtual_memory = psutil.virtual_memory()

        data = [
            ("virt_mem_total", virtual_memory.total, units),
            ("virt_mem_available", virtual_memory.available, units),
            ("virt_mem_used", virtual_memory.used, units),
            ("virt_mem_free", virtual_memory.free, units),
        ]

        self.save_metrics(data)

    def save_metrics(self, data):
        for metric_values in data:
            metric_kwargs = dict(zip(self.metric_keys, metric_values))
            metric = Metric.parse_obj(metric_kwargs)
            metric_model = MetricModel(ts=int(time()),metric=metric, meta=self.meta)
            self.metrics_models.append(metric_model)


# ac = AgentCollector(configuration_file="/home/nata/Python/git_lessons15+/level_up_lessons/metric_collector/agent/configs/agent.yaml")
ac = AgentCollector(configuration_file="configs/agent.yaml")
ac.collect_cpu_metrics()
ac.collect_memory_metrics()
