GPU_COMMAND = "nvidia-smi --format=csv --query-gpu=timestamp,name,index,utilization.gpu,memory.total,memory.used,temperature.gpu,power.draw"
GPU_COLUMNS = ["timestamp", "name", "index", "utilization", "total_memory", "used_memory", "temperature", "power"]

CPU_COMMAND = "top -n 1 -b | head -n 5"
CPU_REGEX = [r"([0-9.]+) id"]
CPU_COLUMNS = ["idel"]

MEM_COMMAND = "cat /proc/meminfo"
MEM_REGEX = [
    r"MemTotal:\s+([0-9.]+) kB",
    r"MemAvailable:\s+([0-9.]+) kB",
    r"SwapTotal:\s+([0-9.]+) kB",
    r"SwapFree:\s+([0-9.]+) kB",
]
MEM_COLUMNS = [
    "total_memory",
    "used_memory",
    "total_swap",
    "used_swap",
]
