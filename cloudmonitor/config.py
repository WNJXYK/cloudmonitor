import os
import copy
import yaml
import logging

__all__ = ["C", "load_config", "load_args"]


class Config:
    def __init__(self, default_conf):
        self.__dict__["_default_config"] = copy.deepcopy(default_conf)  # avoiding conflictions with __getattr__
        self.reset()

    def __getitem__(self, key):
        return self.__dict__["_config"][key]

    def __getattr__(self, attr):
        if attr in self.__dict__["_config"]:
            return self.__dict__["_config"][attr]

        raise AttributeError(f"No such {attr} in self._config")

    def get(self, key, default=None):
        return self.__dict__["_config"].get(key, default)

    def __setitem__(self, key, value):
        self.__dict__["_config"][key] = value

    def __setattr__(self, attr, value):
        self.__dict__["_config"][attr] = value

    def __contains__(self, item):
        return item in self.__dict__["_config"]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __str__(self):
        return str(self.__dict__["_config"])

    def __repr__(self):
        return str(self.__dict__["_config"])

    def reset(self):
        self.__dict__["_config"] = copy.deepcopy(self._default_config)

    def update(self, *args, **kwargs):
        self.__dict__["_config"].update(*args, **kwargs)


def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as fr:
            config = yaml.load(fr, yaml.FullLoader)
            # Apply config files to config
            C.servers = config["servers"]
            if "refresh" in config:
                C.refresh = float(config["refresh"])
            if "workers" in config:
                C.workers = int(config["workers"])
            if "port" in config:
                C.port = int(config["port"])

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


def load_args(args):
    C.workers = args.workers
    C.port = args.port


ROOT_DIRPATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(os.path.expanduser('~'), "templates")

_DEFAULT_CONFIG = {
    "root_path": ROOT_DIRPATH,
    "template_path": TEMPLATE_PATH,
    "servers": {},
    "refresh": 60,
    "status": {},
    "workers": 4,
    "port": 8899,
}

C = Config(_DEFAULT_CONFIG)
