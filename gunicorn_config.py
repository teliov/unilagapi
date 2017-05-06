import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config as cfg
import pwd

PWD_UID = 2
PWD_GID = 3

pwd_data = pwd.getpwnam("www-data")
user_uid = pwd_data[PWD_UID]
user_gid = pwd_data[PWD_GID]

curr_path = os.path.dirname(__file__)

cfg.init()

port = os.environ.get("BIND_PORT")

# Server
bind = "127.0.0.1:" +  str(port)

# Worker Processes
worker = 1

# Server Mechanics
# user = int(user_uid)
# group = int(user_gid)


# Logging
accesslog = os.path.abspath(os.path.join(curr_path, "access.log"))
errorlog = os.path.abspath(os.path.join(curr_path, "error.log"))
loglevel = os.environ.get("LOG_LEVEL") or "warning"