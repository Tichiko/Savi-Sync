import psutil
import time
from sync import run_ludusavi

def monitor_game_process(config):
    print("Monitoring for game processes...")
    known_steam_games = ["eldenring.exe", "hades.exe"]  # Customize this

    while True:
        found = None
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in known_steam_games:
                found = proc
                print(f"Detected running game: {proc.info['name']}")
                break

        if found:
            found.wait()
            print("Game closed. Syncing...")
            run_ludusavi(config, "backup")
            return
        time.sleep(5)