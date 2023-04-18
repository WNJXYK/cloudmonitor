import time, logging
from .define import COLUMNS, COMMAND
from ..config import C
from ..ssh import exec_command

__all__ = ["update_gpu"]

def parse_gpu(opt):
    ret = []
    for i in range(1, len(opt)):
        items = opt[i].strip().split(sep=',')
        items = [x.strip() for x in items]
        gpu_status = { "updated": time.time() }
        for j in range(len(COLUMNS)):
            gpu_status[COLUMNS[j]] = items[j]
        ret.append(gpu_status)
    return ret

def update_gpu(servers):
    gpus = {}
    
    # Process each server
    for server_name in servers:
        server_config = servers[server_name]
        server_name = str(server_name)
        
        # Exec GPU commands
        try:
            opt, _ = exec_command(server_config, COMMAND)
        except Exception as err:
            logging.error(f"[GPU] {server_name} {err}")
        
        # Process GPU info
        try:
            gpus[server_name] = parse_gpu(opt)
        except:
            logging.error(f"[GPU] {server_name} GPU status process failed.")
    
    return gpus