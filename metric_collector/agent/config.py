from ruamel.yaml import YAML


class AgentConfig:
    source_name = None
    interval = None
    cpu = False
    memory = False
    host_identificator = 0
    agent_yaml = YAML()
    config = {}

    def __init__(self, configuration_file):
        self.__config_file = configuration_file
        self.parse_config()

    def load_config_from_yaml(self) -> dict:
        with open(self.__config_file, "r") as f:
            return self.agent_yaml.load(f)

    def parse_config(self):
        class_variables = AgentConfig.__dict__.keys()
        self.config = self.load_config_from_yaml()
        # print(self.config)
        for key, value in self.config.items():
            if key in class_variables:
                value = self.transform_values(key, value)
                setattr(AgentConfig, key, value)

    def transform_values(self, key, value):
        transformation_mapper = {
            "interval": self.transform_interval,
            "host_identificator": self.transform_identificator
        }
        transformator = transformation_mapper.get(key)
        if transformator:
            return transformator(value)
        else:
            return value

    def transform_interval(self):
        pass


    def transform_identificator(self):
        pass



ag = AgentConfig("./agent/configs/agent.yaml")
