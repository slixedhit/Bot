import logging
from discord.ext import commands
import discord

logger = logging.getLogger("bot.errors")


def register_error_handlers(bot: commands.Bot):
    @bot.event
    async def on_command_error(ctx: commands.Context, error: commands.CommandError):
        # Basic global handler for prefix commands
        if isinstance(error, commands.CommandNotFound):
            return
        try:
            await ctx.reply(f"Error: {error}")
        except Exception:
            logger.exception("Failed to send command error")

    @bot.event
    async def on_application_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
        # Basic global handler for slash commands
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"Error: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Error: {error}", ephemeral=True)
        except Exception:
            logger.exception("Failed to send app command error")
