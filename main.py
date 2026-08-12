"""Main entry point for the bot.

Run with: DISCORD_TOKEN in environment or .env file.
"""
import asyncio
import os
import sys
from pathlib import Path

import discord
from discord.ext import commands

from core.config import Config
from core.logging_setup import setup_logging
from core.database import Database
from core.errors import register_error_handlers
from core.scheduler import scheduler

ROOT = Path(__file__).parent


def load_cogs(bot: commands.Bot):
    cogs_dir = ROOT / "cogs"
    for file in sorted(cogs_dir.glob("*.py")):
        if file.name.startswith("__"):
            continue
        ext = f"cogs.{file.stem}"
        try:
            bot.load_extension(ext)
            bot.logger.info(f"Loaded cog: {ext}")
        except Exception as e:
            bot.logger.exception(f"Failed to load cog {ext}: {e}")


async def main():
    config = Config.from_env()
    setup_logging(config.LOG_LEVEL)

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(
        command_prefix=config.DEFAULT_PREFIX,
        intents=intents,
        application_id=None,  # optional
        help_command=None,
    )

    # attach logger and config to bot for easy access in cogs
    bot.logger = __import__("logging").getLogger("bot")
    bot.config = config

    # Database
    bot.db = await Database.connect(config.DATA_DIRECTORY / "bot.db")

    # Register global error handlers
    register_error_handlers(bot)

    # Start scheduler
    scheduler.start()
    bot.scheduler = scheduler

    # Load cogs
    load_cogs(bot)

    # Register persistent views if any (imported at startup in core.views)
    try:
        import core.views  # noqa: F401
    except Exception:
        bot.logger.exception("Failed to import persistent views")

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        bot.logger.error("DISCORD_TOKEN is not set. Exiting.")
        await bot.db.close()
        return

    try:
        await bot.start(token)
    except KeyboardInterrupt:
        bot.logger.info("Shutting down (KeyboardInterrupt)")
        await bot.close()
    finally:
        await bot.db.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        import logging

        logging.getLogger("bot").exception("Unhandled exception in main", exc_info=e)
        sys.exit(1)
