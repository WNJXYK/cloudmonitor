import paramiko

__all__ = ["exec_command", "exec_commands"]


def exec_command(server_config, command):
    with paramiko.SSHClient() as p:
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p.connect(
            server_config["host"],
            port=server_config["port"],
            username=server_config["username"],
            password=server_config["password"],
        )
        stdin, stdout, stderr = p.exec_command(command)
        opt = stdout.readlines()
        err = stderr.readlines()
    return opt, err


def exec_commands(server_config, command_list):
    with paramiko.SSHClient() as p:
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p.connect(
            server_config["host"],
            port=server_config["port"],
            username=server_config["username"],
            password=server_config["password"],
        )
        ret = []
        for command in command_list:
            stdin, stdout, stderr = p.exec_command(command)
            opt = stdout.readlines()
            err = stderr.readlines()
            ret.append((opt, err))
    return ret
