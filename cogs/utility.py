from discord.ext import commands
import discord
import time


class Utility(commands.Cog):
    """Utility commands like ping, uptime, avatar."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._start_time = time.time()

    @commands.hybrid_command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Check bot latency."""
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f"Pong! {latency}ms")

    @commands.hybrid_command(name="uptime")
    async def uptime(self, ctx: commands.Context):
        """Show uptime."""
        seconds = int(time.time() - self._start_time)
        await ctx.reply(f"Uptime: {seconds} seconds")


async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))
