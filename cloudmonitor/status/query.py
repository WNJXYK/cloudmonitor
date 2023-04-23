import time, logging, re
from multiprocessing import Pool
from .define import *
from ..config import C
from ..ssh import exec_commands

__all__ = ["update_servers"]


def parse_gpu(opt):
    ret = []
    for i in range(1, len(opt)):
        items = opt[i].strip().split(sep=",")
        items = [x.strip() for x in items]
        gpu_status = {"updated": time.time()}
        for j in range(len(GPU_COLUMNS)):
            gpu_status[GPU_COLUMNS[j]] = items[j]
        ret.append(gpu_status)
    return ret


def parse_regex(opt, reg, col):
    assert len(reg) == len(col)
    ret = {}
    lines = " ".join([x.strip() for x in opt])
    for i in range(len(reg)):
        res = re.search(reg[i], lines, re.M | re.I)
        ret[col[i]] = res.group(1)
    return ret


def udpate_server(server_pack):
    server_name, server_config = server_pack
    ret = {"NAME": server_name, "RANK": server_config["rank"], "CONNECT": True}

    # Process Commands
    ssh_flag = True
    try:
        (GPU_opt, _), (CPU_opt, _), (MEM_opt, _) = exec_commands(
            server_config,
            [
                GPU_COMMAND,
                CPU_COMMAND,
                MEM_COMMAND,
            ],
        )
    except Exception as err:
        logging.error(f"[SSH] {server_name} {err}")
        ssh_flag = False
    if not ssh_flag:
        ret["CONNECT"] = False
        return ret

    # Parse Returns
    try:
        ret["GPU"] = parse_gpu(GPU_opt)
    except:
        logging.error(f"[GPU] {server_name} GPU status process failed.")
    try:
        ret["CPU"] = parse_regex(CPU_opt, CPU_REGEX, CPU_COLUMNS)
    except Exception as err:
        logging.error(f"[CPU] {server_name} system status process failed.")
    try:
        ret["MEM"] = parse_regex(MEM_opt, MEM_REGEX, MEM_COLUMNS)
    except Exception as err:
        logging.error(f"[MEM] {server_name} memory status process failed.")

    return ret


def update_servers(servers):
    ret = {}

    # Process each server
    configs = []
    for server_name in servers:
        server_config = servers[server_name]
        server_name = str(server_name)
        configs.append((server_name, server_config))
    with Pool(C.workers) as mpc:
        ret = mpc.map(udpate_server, configs)

    # Sort servers
    ret = sorted(ret, key=lambda item: item["RANK"])
    return ret
