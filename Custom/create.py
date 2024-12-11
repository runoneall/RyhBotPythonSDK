import shutil
import os
import json
from .templates.message import template as message_template
from .templates.server import template as server_template

root_dir = "RyhBotPythonSDK"
plugins_dir = f"{root_dir}/plugin"

if os.path.exists(root_dir):
    shutil.rmtree(root_dir)
os.mkdir(root_dir)

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

