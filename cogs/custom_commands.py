from discord.ext import commands
import discord


class CustomCommands(commands.Cog):
    """Custom commands and embeds skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="customcommand")
    async def customcommand(self, ctx: commands.Context, action: str = "list"):
        await ctx.reply("Custom command management placeholder")

    @commands.hybrid_command(name="embed")
    async def embed(self, ctx: commands.Context, action: str = "say"):
        await ctx.reply("Embed create/send placeholder")


async def setup(bot: commands.Bot):
    await bot.add_cog(CustomCommands(bot))
