# Game Sync Tool

A cross-platform save sync utility that wraps around [Ludusavi](https://github.com/mtkennerly/ludusavi) and integrates with [Syncthing](https://syncthing.net/). Designed with Steam Deck and PC in mind.

## Features

- Cross-platform: Steam Deck (Linux), Linux desktop, Windows
- Configurable via JSON file
- Syncs game saves after game exit
- CLI-based with future GUI integration support
- Modular sync system (Syncthing support now, more later)
- Auto-detection of dependencies

## Usage

```bash
python main.py -setup        # Initial setup
python main.py -backup       # Run Ludusavi backup
python main.py -restore      # Run Ludusavi restore
python main.py -sync         # Monitor for game process and sync on exit
python main.py -ludusavi     # Launch Ludusavi GUI
python main.py -syncthing    # Open Syncthing config page
```

## Dependencies

- Python 3.8+
- `psutil` (install with `pip install -r requirements.txt`)
- Ludusavi (CLI)
- Syncthing

## License

MIT
