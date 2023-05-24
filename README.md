# Cloud Monitor: 面向学术的服务器监控程序

<p align="center">
    <a href="https://pypi.org/project/cloudmonitor/"><img src="https://badgen.net/pypi/v/cloudmonitor"></a>
    <a href="#"><img src="https://badgen.net/github/stars/WNJXYK/cloudmonitor"></a>
    <a href="https://pepy.tech/project/cloudmonitor"><img src="https://pepy.tech/badge/cloudmonitor"></a>
    <a href="#"><img src="https://img.shields.io/github/last-commit/WNJXYK/cloudmonitor"></a>
    <!-- <a href="https://coveralls.io/github/WNJXYK/cloudmonitor?branch=master"><img src="https://coveralls.io/repos/github/WNJXYK/cloudmonitor/badge.svg?branch=master"></a> -->
</p>

## Navigation

| Navigation |  Quick Start |
| :----: | :---- |
| English |  [Quick Start](#quick-start) |
| Chinese |  [快速开始](#快速开始) |

## 更新
  
* 🌟 2023/05/24：初始版本发布
  * 实现了服务器的 GPU、CPU、Memory、Swap 使用情况监控。

## Quick Start

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
    rank: 1            # Display Priority (1-999)
  Server-2:            # Server nickname (unique)
    host: 192.168.31.2 # IP address of the server
    password: password # Password of the server
    username: root     # Username of the server
    rank: 1            # Display Priority (1-999)
    port: 21599        # The port of the server, default is 22
```
3. Start Cloud Monitor by running the command `cloudmonitor -c \home\user\config.yaml`, and you can use the created configuration file to start a server monitoring web service.

Ultimately, the monitoring program will run at "0.0.0.0:port".

## 快速开始

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
    rank: 999          # 服务器的显示顺序(1-999)
  Server-2:            # 服务器昵称（唯一）
    host: 192.168.31.2 # 服务器的IP地址
    password: password # 服务器的密码
    username: root     # 服务器的用户名
    rank: 1            # 服务器的显示顺序(1-999)
    port: 21599        # 服务器的端口，缺省为 22
```
3. 启动 Cloud Monitor，运行命令 `cloudmonitor -c \home\user\config.yaml`，即可使用配置文件创建服务器监控网页。

最终，监控程序将运行在 "0.0.0.0:port" 地址。

## Preview

![Preview](https://github.com/WNJXYK/cloudmonitor/blob/master/images/Example.png?raw=true)