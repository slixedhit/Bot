from discord.ext import commands
import discord


class Welcome(commands.Cog):
    """Welcome/goodbye and verification skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        # Simple welcome direct message (can be extended to channel welcomes)
        try:
            await member.send(f"Welcome to {member.guild.name}, {member.display_name}!")
        except Exception:
            pass


async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))
