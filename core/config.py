from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Config:
    DISCORD_TOKEN: Optional[str]
    BOT_OWNER_IDS: list[int]
    DEV_GUILD_ID: Optional[int]
    DEFAULT_PREFIX: str
    DATA_DIRECTORY: Path
    LOG_LEVEL: str

    @classmethod
    def from_env(cls) -> "Config":
        data_dir = Path(os.getenv("DATA_DIRECTORY", "data"))
        data_dir.mkdir(parents=True, exist_ok=True)
        return cls(
            DISCORD_TOKEN=os.getenv("DISCORD_TOKEN"),
            BOT_OWNER_IDS=[int(x) for x in os.getenv("BOT_OWNER_IDS", "").split(",") if x.strip()],
            DEV_GUILD_ID=int(os.getenv("DEV_GUILD_ID")) if os.getenv("DEV_GUILD_ID") else None,
            DEFAULT_PREFIX=os.getenv("DEFAULT_PREFIX", "!"),
            DATA_DIRECTORY=data_dir,
            LOG_LEVEL=os.getenv("LOG_LEVEL", "INFO"),
        )
