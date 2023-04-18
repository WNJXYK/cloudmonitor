from flask import Flask, render_template, jsonify
import time
import argparse, yaml
import logging
import functools
from datetime import datetime, timedelta
from .config import C
from .gpu import update_gpu

__all__ = ["main"]

app = Flask(__name__)
parser = argparse.ArgumentParser(
    prog='Cloud Monitor',
    description='A Web-GUI for monitoring servers',
    # epilog='Text at the bottom of help'
)
parser.add_argument('-c', "--config", dest="config", required=True,  type=str, help='path of YAML config file')
parser.add_argument('-p', "--port",   dest="port",   required=False, default=8899, type=int, help='port for Web GUI')
args = parser.parse_args()

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


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/reload')
def reload():
    if not load_config(args.config): return "Error! Please see logs."
    return "Config reloaded."

@app.route('/gpu')
@cache(seconds=C.gpu_refresh)
def gpu_status():
    C.gpus = update_gpu(C.servers)
    return jsonify(C.gpus)

def load_config(path):
    try:
        with open(args.config, 'r', encoding='utf-8') as fr:
            config = yaml.load(fr, yaml.FullLoader)
            # Apply config files to config
            C.servers = config["servers"]
            if "gpu_refresh" in config: C.gpu_refresh = float(config["gpu_refresh"])
            
        # Set default key-value in config
        for server_name in C.servers:
            if "port" not in C.servers[server_name]:
                C.servers[server_name]["port"] = 22
            if "rank" not in C.servers[server_name]:
                C.servers[server_name]["rank"] = 999
            if "path" not in C.servers[server_name]:
                C.servers[server_name]["path"] = ["/"]
    except Exception as err:
        logging.error(f"[CONFIG] Load config error: {err}.")
        return False
    return True

def main():
    if not load_config(args.config): exit(0)
    app.run(host='127.0.0.1', port=args.port, debug=True)

if __name__ == "__main__": main()
    