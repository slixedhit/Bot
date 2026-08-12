# Bot README

This repository is a scaffold for a Discord bot built with discord.py 2.x.

Requirements
- Python 3.11+
- See requirements.txt

Setup
1. Copy `.env.example` to `.env` and set DISCORD_TOKEN.
2. (Optional) Set `BOT_OWNER_IDS` in `.env` to a comma-separated list of developer user IDs who should have access to developer commands. Example:
   BOT_OWNER_IDS=556152136648622082
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run: `python main.py`

Project layout
- main.py - entrypoint
- cogs/ - feature modules (moderation, tickets, welcome, ...)
- core/ - configuration, database, scheduler, utils
- data/ - runtime data directory (created automatically)

Developer commands
- `dev sync` - Sync application (slash) commands globally. Restricted to BOT_OWNER_IDS or the application owner.
- `dev info` - Show simple bot info for developers.

This scaffold implements a minimal, self-contained bot and database
initialization. Many commands are placeholders with TODO markers so you can
extend functionality incrementally.
