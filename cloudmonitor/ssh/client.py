import paramiko

__all__ = ["exec_command"]

def exec_command(server_config, command):
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p.connect(
        server_config["host"], 
        port=server_config["port"], 
        username=server_config["username"],
        password=server_config["password"]
    )
    stdin, stdout, stderr = p.exec_command(command)
    opt = stdout.readlines()
    err = stderr.readlines()
    return opt, err