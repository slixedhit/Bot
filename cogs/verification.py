from discord.ext import commands
import discord


class Verification(commands.Cog):
    """Verification, welcome, and rules skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_group(name="verify", invoke_without_command=True)
    async def verify(self, ctx: commands.Context):
        await ctx.reply("Use verify subcommands: setup, panel, role, unverified-role, channel, timeout, approve, deny, reset")

    @verify.command(name="panel")
    async def panel(self, ctx: commands.Context):
        # send a simple button panel using core.views if available
        try:
            from core.views import ticket_create_view
            await ctx.reply("Verification panel (placeholder)", view=ticket_create_view)
        except Exception:
            await ctx.reply("Verification panel (placeholder)")

    @commands.hybrid_command(name="rules")
    async def rules(self, ctx: commands.Context, action: str = "view"):
        await ctx.reply("Server rules: (placeholder)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Verification(bot))
