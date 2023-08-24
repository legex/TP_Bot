import logging
from webex_bot.models.command import Command
from datetime import*
import re
from AdminGuide_Main import*

log = logging.getLogger(__name__)

# Get a free account at openweathermap.org &
# insert API key here:
class AdminGuides(Command):
    def __init__(self):
        # Define custom command info here
        # command_keyword = what chat keyword will trigger this command to execute
        # help_message = what message is returned when user sends 'help' message
        # card = optionally send an AdaptiveCard response
        super().__init__(
            command_keyword="admin guide" or "Admin guide",
            help_message="Admin guide Syntax: admin guide devicetype",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # By default, command keyword will be stripped out before being passed to execute function
        # Need to strip the additional whitespace around the input:
        valid_input=str(message)
        ptrn = r'([aA-zZ]{2}\d{2,3})|([r,c][aA-zZ]{3,12}.\d{2}.{0,1})|((roomkit).{0,5})'
        match=re.search(ptrn, valid_input)
        while match!= None:
            try:
                vc_unit=match.group()
            except:
                print("Unable to match")
            break
        #Since callback command will be stripped, taking rest of the input to store in a variable
        devices=vc_unit.upper()
        # Using the variable to extract required links
        adg=AdminGuide_Main(devices)
        guides_fin=adg.curated_guide()
        serial_num=[]

        for serial in range(1,len(guides_fin)+1):
            serial_num.append(serial)
        output_links='''
        '''
        for a,b in zip(serial_num, guides_fin):
            output_links += str(a)+' ' +b +'\n'
        return output_links

        # Message returned will be sent back to the user by bot
