<p align="center">
  <img src="savi sync logo.png" alt="Savi Sync Logo" width="200"/>
</p>
# Savi Sync

**Savi Sync** is a cross-platform game save sync utility currently in development. Its goal is to make syncing game saves easy and reliable for games that don’t support native or platform-based cloud saving (e.g., Steam Cloud or Epic Games Cloud Saves).

Savi Sync wraps around [Ludusavi](https://github.com/mtkennerly/ludusavi) and integrates with [Syncthing](https://syncthing.net/) to create a seamless syncing experience. While it’s designed primarily with the **Steam Deck** in mind, it also supports **Linux desktops** and **Windows**.

> ⚠️ **Note:** macOS is not officially supported at this time. However, as an open source project, contributions for macOS compatibility are welcome.

## Features

- Cross-platform: Steam Deck (SteamOS), Linux desktop, Windows
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

This project is licensed under the terms of the **GNU General Public License v3.0**.
See the [LICENSE](LICENSE) file for details.
