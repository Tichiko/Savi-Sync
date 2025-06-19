import json
import os
from shutil import which

CONFIG_PATH = "config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

def setup_config():
    config = {}

    # Try to locate Ludusavi
    ludusavi = which("ludusavi")
    if not ludusavi:
        ludusavi = input("Enter path to Ludusavi executable: ")
    config["ludusavi_path"] = ludusavi

    # Try to locate Syncthing
    syncthing = which("syncthing")
    if not syncthing:
        syncthing = input("Enter path to Syncthing executable: ")
    config["syncthing_path"] = syncthing

    config["syncthing_web_url"] = "http://127.0.0.1:8384"

    save_config(config)
    print("Setup complete.")