from discord.ext import commands
import discord
from core.checks import is_dev


class Dev(commands.Cog):
    """Developer-only utilities. Only usable by IDs in BOT_OWNER_IDS or the app owner."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_group(name="dev", invoke_without_command=True)
    @is_dev()
    async def dev(self, ctx: commands.Context):
        await ctx.reply("Dev commands: sync, info")

    @dev.command(name="sync")
    @is_dev()
    async def sync(self, ctx: commands.Context):
        """Sync application commands globally."""
        await ctx.defer()
        try:
            synced = await ctx.bot.tree.sync()
            await ctx.followup.send(f"Synced {len(synced)} commands globally.")
        except Exception as e:
            await ctx.followup.send(f"Sync failed: {e}")

    @dev.command(name="info")
    @is_dev()
    async def info(self, ctx: commands.Context):
        """Show bot info useful to developers."""
        cfg = getattr(self.bot, "config", None)
        owner_ids = cfg.BOT_OWNER_IDS if cfg else []
        await ctx.reply(f"Bot: {self.bot.user}\nOwners: {owner_ids}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))
