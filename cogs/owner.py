from discord.ext import commands
import discord


class Owner(commands.Cog):
    """Owner-only commands: about, shutdown, reload."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="shutdown")
    async def shutdown(self, ctx: commands.Context):
        await ctx.send("Shutting down...")
        await ctx.bot.close()

    @commands.is_owner()
    @commands.command(name="reloadcogs")
    async def reloadcogs(self, ctx: commands.Context):
        count = 0
        for ext in list(ctx.bot.extensions.keys()):
            try:
                ctx.bot.reload_extension(ext)
                count += 1
            except Exception:
                pass
        await ctx.send(f"Reloaded {count} extensions")


async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
