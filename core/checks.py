from discord.ext import commands
from discord import app_commands


def is_admin():
    async def predicate(ctx: commands.Context):
        if ctx.guild is None:
            return False
        return ctx.author.guild_permissions.administrator

    return commands.check(predicate)


def is_owner():
    async def predicate(ctx: commands.Context):
        app = await ctx.bot.application_info()
        return ctx.author.id == app.owner.id

    return commands.check(predicate)


def is_dev():
    async def predicate(ctx: commands.Context):
        # allow IDs in BOT_OWNER_IDS env or application owner
        bot = ctx.bot
        try:
            if hasattr(bot, "config") and getattr(bot.config, "BOT_OWNER_IDS", None):
                if ctx.author.id in bot.config.BOT_OWNER_IDS:
                    return True
        except Exception:
            pass
        app = await bot.application_info()
        return ctx.author.id == app.owner.id

    return commands.check(predicate)
