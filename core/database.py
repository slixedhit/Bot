"""Simple async SQLite helper and schema initialization."""
from pathlib import Path
import aiosqlite
import asyncio
from typing import Optional

CREATE_TABLES_SQL = r'''
CREATE TABLE IF NOT EXISTS settings (
    guild_id INTEGER PRIMARY KEY,
    prefix TEXT DEFAULT '!'
);

CREATE TABLE IF NOT EXISTS cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id INTEGER,
    moderator_id INTEGER,
    target_id INTEGER,
    action TEXT,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NULL,
    reversed INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS warnings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id INTEGER,
    user_id INTEGER,
    moderator_id INTEGER,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guild_id INTEGER,
    message TEXT,
    remind_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guild_id INTEGER,
    channel_id INTEGER,
    user_id INTEGER,
    status TEXT DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''


class Database:
    def __init__(self, db: aiosqlite.Connection):
        self._db = db

    @classmethod
    async def connect(cls, path: Path) -> "Database":
        path.parent.mkdir(parents=True, exist_ok=True)
        db = await aiosqlite.connect(path)
        # enable WAL for better concurrency
        await db.execute("PRAGMA journal_mode=WAL;")
        await db.commit()
        await cls._initialize(db)
        return cls(db)

    @staticmethod
    async def _initialize(conn: aiosqlite.Connection):
        await conn.executescript(CREATE_TABLES_SQL)
        await conn.commit()

    async def execute(self, *args, **kwargs):
        return await self._db.execute(*args, **kwargs)

    async def fetchall(self, query, params=()):
        cur = await self._db.execute(query, params)
        rows = await cur.fetchall()
        await cur.close()
        return rows

    async def fetchone(self, query, params=()):
        cur = await self._db.execute(query, params)
        row = await cur.fetchone()
        await cur.close()
        return row

    async def close(self):
        await self._db.close()
