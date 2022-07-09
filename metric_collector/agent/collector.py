from typing import List

from config import AgentConfig
import psutil
from metric import Metric


class AgentCollector(AgentConfig):

    def __init__(self, *args, **kwargs):
        self.metrics: List[Metric] = [] # в этот пустой спислк будут записаны метрики класса Metric
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

        for metric in data:
            # мы проитерируемся по data и добавим в пустой список self.metrics объекты класса Metric с атрибутами
            self.metrics.append(Metric(*metric))

    def collect_memory_metrics(self):
        """
        descr: Return statistics about system memory usage
        units: bytes
        :return: None
        """
        units = "bytes"
        virtual_memory = psutil.virtual_memory()

        data = [
            ("virt_mem_total", virtual_memory.total, units),
            ("virt_mem_available", virtual_memory.available, units),
            ("virt_mem_used", virtual_memory.used, units),
            ("virt_mem_free", virtual_memory.free, units),
        ]

        for metric in data:
            self.metrics.append(Metric(*metric))


# ac = AgentCollector(configuration_file="/home/nata/Python/git_lessons15+/level_up_lessons/metric_collector/agent/configs/agent.yaml")
ac = AgentCollector(configuration_file="./configs/agent.yaml")
ac.collect_cpu_metrics()
ac.collect_memory_metrics()
