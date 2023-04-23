from flask import Flask, render_template, jsonify
import time
import argparse, yaml
import logging
import functools
from datetime import datetime, timedelta
from .config import C, load_config, load_args
from .status import update_servers

__all__ = ["main"]

app = Flask(__name__)
parser = argparse.ArgumentParser(
    prog="Cloud Monitor",
    description="A Web-GUI for monitoring servers",
    # epilog='Text at the bottom of help'
)
parser.add_argument("-c", "--config", dest="config", required=True, type=str, help="path of YAML config file")
parser.add_argument("-p", "--port", dest="port", required=False, default=8899, type=int, help="port for Web GUI")
parser.add_argument(
    "-w", "--workers", dest="workers", required=False, default=4, type=int, help="number of multi-process workers"
)
args = parser.parse_args()
load_args(args)
if not load_config(args.config):
    exit(0)


def cache(seconds: int, maxsize: int = 128, typed: bool = False):
    def wrapper_cache(func):
        func = functools.lru_cache(maxsize=maxsize, typed=typed)(func)
        func.delta = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.delta

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.delta
            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@app.route("/")
def hello_world():
    status()
    return render_template(os.path.join(C.root_path, "index.html"), servers=C.status)


@app.route("/reload")
def reload():
    if not load_config(args.config):
        return "Error! Please see logs."
    return "Config reloaded."


@app.route("/status")
@cache(seconds=C.refresh)
def status():
    C.status = update_servers(C.servers)
    return jsonify(C.status)


def main():
    app.run(host="0.0.0.0", port=C.port, debug=True)


if __name__ == "__main__":
    main()
