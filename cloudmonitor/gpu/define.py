__all__ = [ "COMMAND", "COLUMNS" ]

COMMAND = "nvidia-smi --format=csv --query-gpu=timestamp,name,index,utilization.gpu,memory.total,memory.used,temperature.gpu,power.draw"
COLUMNS = ["timestamp", "name", "index", "utilization", "memory", "totalmemory", "temperature", "power"]