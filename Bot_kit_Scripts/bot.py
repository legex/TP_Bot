import os
from tokenize import group

from webex_bot.webex_bot import WebexBot
from PeripheralTshoot import Peripherals
from DeviceType import Devicetype
from Issues import Tshoot
from AdminGuides import AdminGuide

# Set Webex API key as the WEBEX_TOKEN environment variable &
# we'll retrieve that here:
webex_token = "Enter_your_Token_Here"

# Bot only needs the Webex token, but optionally we can also
# restrict who the bot will respond to by user or domain.
# For example:
# Restrict by user: WebexBot(webex_token, approved_users=['user@example.local'])
# Restrict by domain: WebexBot(webex_token, approved_domains=['example.local'])
bot = WebexBot(webex_token, approved_rooms= any, approved_domains="cisco.com")

# Registed custom command with the bot:
bot.add_command(Devicetype())
bot.add_command(Tshoot())
bot.add_command(Peripherals())
bot.add_command(AdminGuide())
# Connect to Webex & start bot listener:
bot.run()
