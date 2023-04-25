![pypi](https://badgen.net/pypi/v/cloudmonitor)
![visitors](https://visitor-badge.glitch.me/badge?page_id=WNJXYK.cloudmonitor)
[![Downloads](https://pepy.tech/badge/cloudmonitor)](https://pepy.tech/project/cloudmonitor)

### ATTENTION!

This project is currently under development…

## Navigation

| Navigation | Manual | Quick Start |
| :----: | :---- | :---- |
| English | [Manual](#manual) |  [Quick Start](#quick-start)|
| Chinese | [手册](#手册) | [快速开始](#快速开始) |

## Manual

### Quick Start

1. Install Cloud Monitor by running the command `pip install cloudmonitor`.
2. Create a `config.yaml` file, assuming it is saved in `\home\user\config.yaml`. The format is as follows. Please modify, add or delete the contents according to the specific situation:
```yaml
# Parameter settings
refresh: 10            # Server information refresh interval. Please leave enough refresh time, default is 60
workers: 4             # Number of threads for pulling server information, default is 4
port: 8088             # The port on which the Web service runs, default is 8899

# Server list
servers:
  Server-1:            # Server nickname (unique)
    host: 192.168.31.1 # IP address of the server
    password: password # Password of the server
    username: root     # Username of the server
  Server-2:            # Server nickname (unique)
    host: 192.168.31.1 # IP address of the server
    password: password # Password of the server
    username: root     # Username of the server
    port: 21599        # The port of the server, default is 22
```
3. Start Cloud Monitor by running the command `cloudmonitor -c \home\user\config.yaml`, and you can use the created configuration file to start a server monitoring web service.

## 手册

### 快速开始

1. 安装 Cloud Monitor，运行命令 `pip install cloudmonitor`。
2. 请创建 `config.yaml`，假设保存于 `\home\user\config.yaml`。格式如下，内容请按照具体情况修改、添加或删除：
```yaml
# 参数设置
refresh: 10            # 服务器信息刷新间隔。请留出足够的刷新时间，缺省为 60
workers: 4             # 拉去服务器信息的线程数量，缺省为 4
port: 8088             # Web服务运行的端口，缺省为 8899

# 服务器列表
servers:
  Server-1:            # 服务器昵称（唯一）
    host: 192.168.31.1 # 服务器的IP地址
    password: password # 服务器的密码
    username: root     # 服务器的用户名
  Server-2:            # 服务器昵称（唯一）
    host: 192.168.31.1 # 服务器的IP地址
    password: password # 服务器的密码
    username: root     # 服务器的用户名
    port: 21599        # 服务器的端口，缺省为 22
```
3. 启动 Cloud Monitor，运行命令 `cloudmonitor -c \home\user\config.yaml`，即可使用配置文件创建服务器监控网页。