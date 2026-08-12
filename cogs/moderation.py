from discord.ext import commands
import discord
from core.checks import is_admin


class Moderation(commands.Cog):
    """Moderation commands and case system (skeleton)."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="warn")
    @is_admin()
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = "No reason provided"):
        """Warn a member and create a case."""
        # Create case in DB
        query = "INSERT INTO warnings (guild_id, user_id, moderator_id, reason) VALUES (?, ?, ?, ?)"
        await self.bot.db.execute(query, (ctx.guild.id, member.id, ctx.author.id, reason))
        await self.bot.db._db.commit()
        await ctx.reply(f"{member.mention} has been warned. Reason: {reason}")

    @commands.hybrid_command(name="warnings")
    async def warnings(self, ctx: commands.Context, member: discord.Member = None):
        """List warnings for a member."""
        member = member or ctx.author
        rows = await self.bot.db.fetchall("SELECT id, moderator_id, reason, created_at FROM warnings WHERE guild_id = ? AND user_id = ? ORDER BY created_at DESC", (ctx.guild.id, member.id))
        if not rows:
            await ctx.reply("No warnings found.")
            return
        text = "\n".join([f"{r[0]} | by {r[1]} | {r[2]} | {r[3]}" for r in rows[:10]])
        await ctx.reply(f"Warnings for {member.mention}:\n{text}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))
