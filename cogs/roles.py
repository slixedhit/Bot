from discord.ext import commands
import discord


class Roles(commands.Cog):
    """Role utilities: role menus, selfrole, massrole."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="selfrole")
    async def selfrole(self, ctx: commands.Context, action: str = "list"):
        await ctx.reply("Selfrole command placeholder")

    @commands.hybrid_command(name="massrole")
    async def massrole(self, ctx: commands.Context, sub: str, role: discord.Role, *, members: str = ""):
        await ctx.reply(f"massrole {sub} {role} on {members} (placeholder)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))
