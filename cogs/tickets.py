from discord.ext import commands
import discord


class Tickets(commands.Cog):
    """Ticket system skeleton."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="ticket")
    async def ticket(self, ctx: commands.Context, action: str = "create"):
        """Create or manage tickets (very small skeleton)."""
        if action == "create":
            ch = await ctx.guild.create_text_channel(f"ticket-{ctx.author.name}")
            await self.bot.db.execute("INSERT INTO tickets (guild_id, channel_id, user_id) VALUES (?, ?, ?)", (ctx.guild.id, ch.id, ctx.author.id))
            await self.bot.db._db.commit()
            await ctx.reply(f"Created ticket: {ch.mention}")
        else:
            await ctx.reply("Unknown ticket action")


async def setup(bot: commands.Bot):
    await bot.add_cog(Tickets(bot))
