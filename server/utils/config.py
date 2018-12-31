from functools import lru_cache
from os import getcwd
import json


@lru_cache(maxsize=1)
def read(is_dev):
    env = "dev" if is_dev else "prod"
    with open(str.format("{cwd}/config/config.{env}.json", cwd=getcwd(), env=env)) as f:
        return json.load(f)
