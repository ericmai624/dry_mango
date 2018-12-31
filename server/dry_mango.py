from flask import Flask, render_template
from http import HTTPStatus
from pymongo import MongoClient
from services.crawler import crawler
from utils import config

app = Flask(
    __name__, template_folder="../client/dist", static_folder="../client/dist/static"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crawl", methods=["POST"])
def crawl():
    crawler.run("job_opening")
    return ("", HTTPStatus.OK)


def is_dev():
    return app.config["ENV"] != "production"


def connect_db():
    db_config = config.read(is_dev())["database"]
    client = MongoClient(
        str.format(
            "mongodb+srv://{username}:{password}@{host}",
            username=db_config["username"],
            password=db_config["password"],
            host=db_config["host"],
        )
    )
    return client.dry_mango


if __name__ == "__main__":
    app.run()
