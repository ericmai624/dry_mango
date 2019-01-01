from pymongo import MongoClient
from utils import config
from app import is_dev


def connect():
    db_config = config.read(is_dev())["database"]
    client = MongoClient(
        str.format(
            "mongodb+srv://{username}:{password}@{host}",
            username=db_config["username"],
            password=db_config["password"],
            host=db_config["host"],
        )
    )
    return client[db_config["database"]]


def get_collection(collection):
    return connect()[collection]
