from flask import Flask, render_template
from http import HTTPStatus
from services.crawler import crawler

app = Flask(
    __name__, template_folder="../client/dist", static_folder="../client/dist/static"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crawl", methods=["POST"])
def crawl():
    crawler.run("job_openings")
    return ("", HTTPStatus.OK)


def is_dev():
    return app.config["ENV"] != "production"


if __name__ == "__main__":
    app.run()
