"""Persistent UI views (buttons/selects) for tickets, verification, etc.

Register views at import time so discord.py will restore persistent views on
restart if they are created with a timeout=None and previously added.
"""
from discord.ui import View, Button
import discord


class TicketCreateView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(style=discord.ButtonStyle.primary, label="Open Ticket", custom_id="ticket_open"))


# instantiate and expose to main so importing core.views registers it
ticket_create_view = TicketCreateView()

# In main.py, we import core.views to ensure views are instantiated at startup.
