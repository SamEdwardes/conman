from pathlib import Path
import os
import yaml
from pydantic import create_model
import rich

def hello_world():
    print("Hello world)")

class Config:
    def __init__(self, file: str = "config.yml"):
        # Check the active configuration.
        active_environment = os.getenv("CONBUDDY_ACTIVE")
        if active_environment is None:
            active_environment = "default"

        # Load the configuration file.
        with open(Path(file), 'r') as file:
            self.values = yaml.safe_load(file)[active_environment]

    def get(self, key: str):
        return self.values.get(key)

    def __str__(self) -> str:
        return str(self.values)


def load_config(file: str = "config.yml"):
    # Check the active configuration.
    active_environment = os.getenv("CONBUDDY_ACTIVE")
    if active_environment is None:
        active_environment = "default"

    # Load the configuration file.
    with open(Path(file), 'r') as file:
        config_data = yaml.safe_load(file)[active_environment]

    # Parse into a pydantic model.
    ConfigModel = create_model("ConfigModel", **config_data)
    config_model = ConfigModel()
    return config_model