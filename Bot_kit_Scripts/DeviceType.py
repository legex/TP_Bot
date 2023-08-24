import json
import logging
import requests
from webex_bot.models.command import Command

log = logging.getLogger(__name__)

# insert API key here:


class Devicetype(Command):
    def __init__(self):
        # Define custom command info here
        # command_keyword = what chat keyword will trigger this command to execute
        # help_message = what message is returned when user sends 'help' message
        # card = optionally send an AdaptiveCard response
        super().__init__(
            command_keyword="device" or "Device",
            help_message="Share device type.",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # By default, command keyword will be stripped out before being passed to execute function
        # Need to strip the additional whitespace around the input:

        # Message returned will be sent back to the user by bot
        return f"message received: {message}"
