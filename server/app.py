from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__, template_folder="../client/dist", static_folder="../client/dist/static"
)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()