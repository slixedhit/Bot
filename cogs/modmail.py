from discord.ext import commands
import discord


class Modmail(commands.Cog):
    """Simple modmail skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="modmail")
    async def modmail(self, ctx: commands.Context, action: str = "open"):
        await ctx.reply("Modmail placeholder: open/close/list")


async def setup(bot: commands.Bot):
    await bot.add_cog(Modmail(bot))
