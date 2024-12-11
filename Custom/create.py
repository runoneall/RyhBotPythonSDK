import shutil
import os
import json
import server_template
import message_template


root_dir = "RyhBotPythonSDK"
plugins_dir = f"{root_dir}/plugin"

if os.path.exists(root_dir):
    shutil.rmtree(root_dir)
os.mkdir(root_dir)

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

if "message" in config:
    print("Creating message plugin...")

if "server" in config:
    print("Creating server plugin...")

if config['allow-plugin'] == True:
    print("Creating plugin directory...")