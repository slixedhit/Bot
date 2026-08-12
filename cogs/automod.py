from discord.ext import commands
import discord


class Automod(commands.Cog):
    """Automod skeleton with enable/disable and word list management."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_group(name="automod", invoke_without_command=True)
    async def automod(self, ctx: commands.Context):
        await ctx.reply("Use a subcommand: view, enable, disable, words, setup")

    @automod.command(name="view")
    async def view(self, ctx: commands.Context):
        await ctx.reply("Automod settings: (placeholder)")

    @automod.command(name="enable")
    async def enable(self, ctx: commands.Context, feature: str):
        await ctx.reply(f"Enabled automod feature: {feature} (placeholder)")

    @automod.command(name="disable")
    async def disable(self, ctx: commands.Context, feature: str):
        await ctx.reply(f"Disabled automod feature: {feature} (placeholder)")

    @automod.group(name="words", invoke_without_command=True)
    async def words(self, ctx: commands.Context):
        await ctx.reply("Use automod words add/remove/list")

    @words.command(name="add")
    async def words_add(self, ctx: commands.Context, *, word: str):
        await ctx.reply(f"Added word to automod list: {word} (placeholder)")

    @words.command(name="remove")
    async def words_remove(self, ctx: commands.Context, *, word: str):
        await ctx.reply(f"Removed word from automod list: {word} (placeholder)")

    @words.command(name="list")
    async def words_list(self, ctx: commands.Context):
        await ctx.reply("Automod banned words: (placeholder)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Automod(bot))
