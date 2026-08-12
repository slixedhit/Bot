from discord.ext import commands


class Economy(commands.Cog):
    """Economy skeleton with balance and daily commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="balance")
    async def balance(self, ctx: commands.Context, member: commands.MemberConverter = None):
        member = member or ctx.author
        # TODO: implement economy storage
        await ctx.reply(f"{member.display_name} has 0 coins (placeholder)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
