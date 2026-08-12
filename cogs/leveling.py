from discord.ext import commands
import discord


class Leveling(commands.Cog):
    """Leveling and rank skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="rank")
    async def rank(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author
        await ctx.reply(f"{member.display_name} is level 0 (placeholder)")

    @commands.hybrid_command(name="leaderboard")
    async def leaderboard(self, ctx: commands.Context, page: int = 1):
        await ctx.reply("Leaderboard placeholder")


async def setup(bot: commands.Bot):
    await bot.add_cog(Leveling(bot))
