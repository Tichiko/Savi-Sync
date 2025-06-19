import argparse
from config import load_config, save_config, setup_config
from sync import run_ludusavi, open_ludusavi_gui
from sync_methods.syncthing import open_syncthing_gui
from monitor import monitor_game_process

def main():
    parser = argparse.ArgumentParser(description="Game Sync Tool")
    parser.add_argument("-setup", action="store_true", help="Setup tool and detect dependencies")
    parser.add_argument("-sync", action="store_true", help="Run sync after game closes")
    parser.add_argument("-backup", action="store_true", help="Run Ludusavi backup")
    parser.add_argument("-restore", action="store_true", help="Run Ludusavi restore")
    parser.add_argument("-ludusavi", action="store_true", help="Open Ludusavi GUI")
    parser.add_argument("-syncthing", action="store_true", help="Open Syncthing config page")
    args = parser.parse_args()

    config = load_config()

    if args.setup:
        setup_config()
    if args.backup:
        run_ludusavi(config, "backup")
    if args.restore:
        run_ludusavi(config, "restore")
    if args.ludusavi:
        open_ludusavi_gui(config)
    if args.syncthing:
        open_syncthing_gui(config)
    if args.sync:
        monitor_game_process(config)

if __name__ == "__main__":
    main()