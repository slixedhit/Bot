from discord.ext import commands
import discord


class Antiraid(commands.Cog):
    """Anti-raid skeleton with basic commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="raid", invoke_without_command=True)
    async def raid(self, ctx: commands.Context):
        await ctx.reply("Use subcommands: status, setup, enable, disable, mode, threshold, whitelist, quarantine, unlock, recent")

    @raid.command(name="status")
    async def status(self, ctx: commands.Context):
        await ctx.reply("Raid status: OK (placeholder)")

    @raid.command(name="mode")
    async def mode(self, ctx: commands.Context, mode: str):
        await ctx.reply(f"Set raid mode to {mode} (placeholder)")

    @raid.command(name="threshold")
    async def threshold(self, ctx: commands.Context, joins: int, seconds: int):
        await ctx.reply(f"Set raid threshold to {joins} joins in {seconds}s (placeholder)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Antiraid(bot))
