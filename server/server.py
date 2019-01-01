from gevent.pywsgi import WSGIServer
from utils import config
from app import app, is_dev

server_config = config.read(is_dev())["server"]

if __name__ == "__main__":
    host = server_config["host"]
    port = server_config["port"]
    print(str.format("Serving on {}:{}", host, port))
    WSGIServer((host, port), app).serve_forever()
