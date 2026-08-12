from discord.ext import commands


class Owner(commands.Cog):
    """Owner/developer-only commands: about, shutdown, reload."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: commands.Context):
        # allow configured BOT_OWNER_IDS or application owner
        bot = ctx.bot
        if hasattr(bot, "config") and bot.config.BOT_OWNER_IDS:
            if ctx.author.id in bot.config.BOT_OWNER_IDS:
                return True
        app = await bot.application_info()
        return ctx.author.id == app.owner.id

    @commands.command(name="shutdown")
    async def shutdown(self, ctx: commands.Context):
        await ctx.send("Shutting down...")
        await ctx.bot.close()

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
