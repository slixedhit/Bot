from discord.ext import commands
import discord
import random


class Fun(commands.Cog):
    """Fun and games skeleton commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="meme")
    async def meme(self, ctx: commands.Context):
        await ctx.reply("Meme placeholder")

    @commands.hybrid_command(name="joke")
    async def joke(self, ctx: commands.Context):
        jokes = ["Why did the chicken cross the road? To get to the other side!", "I would tell you a UDP joke, but you might not get it."]
        await ctx.reply(random.choice(jokes))

    @commands.hybrid_command(name="coinflip")
    async def coinflip(self, ctx: commands.Context):
        await ctx.reply(random.choice(["Heads", "Tails"]))


async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
