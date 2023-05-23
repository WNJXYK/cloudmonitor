import os
import time
import argparse, yaml
import logging
import functools
from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify
from gevent import pywsgi
from .config import C, load_config, load_args
from .status import update_servers


__all__ = ["main"]

app = Flask(
    __name__,
    template_folder=os.path.join(C.root_path, "templates")
)

parser = argparse.ArgumentParser(
    prog="Cloud Monitor",
    description='''A Web-GUI for monitoring servers''',
    epilog='''Pypi Homepage: https://pypi.org/project/cloudmonitor/'''
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
def index():
    status()
    return render_template("index.html", servers=C.status, refresh=C.refresh)


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
    server = pywsgi.WSGIServer(('0.0.0.0', C.port), app)
    server.serve_forever()

if __name__ == "__main__": main()
