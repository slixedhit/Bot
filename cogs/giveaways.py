from discord.ext import commands
import discord


class Giveaways(commands.Cog):
    """Giveaways skeleton"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="giveaway")
    async def giveaway(self, ctx: commands.Context, action: str = "start"):
        await ctx.reply(f"Giveaway {action} (placeholder)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Giveaways(bot))
