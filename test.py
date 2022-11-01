import os
from rich import print
from conbuddy.main import Config, load_config

os.environ["CONBUDDY_ACTIVE"] = "default"
os.environ["CONBUDDY_ACTIVE"] = "production"

config = load_config()
print(config)

print(config.trials)
