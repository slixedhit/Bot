from discord.ext import commands
import discord


class Settings(commands.Cog):
    """Server settings and backup skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_group(name="settings", invoke_without_command=True)
    async def settings(self, ctx: commands.Context):
        await ctx.reply("Use settings subcommands: view, modules, enable, disable, export, import, backup, restore")

    @settings.command(name="backup")
    async def backup(self, ctx: commands.Context):
        try:
            from core.backup import create_backup
            out = create_backup(self.bot.config.DATA_DIRECTORY)
            await ctx.reply(f"Created backup: {out}")
        except Exception as e:
            await ctx.reply(f"Backup failed: {e}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Settings(bot))
