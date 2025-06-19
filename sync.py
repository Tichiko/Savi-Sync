import subprocess

def run_ludusavi(config, action):
    cmd = [config["ludusavi_path"], action]
    subprocess.run(cmd)

def open_ludusavi_gui(config):
    subprocess.Popen([config["ludusavi_path"]])