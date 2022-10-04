import logging
from webex_bot.models.command import Command
from datetime import*
import re
from Scraper import*

log = logging.getLogger(__name__)

# Get a free account at openweathermap.org &
# insert API key here:

class AdminGuide(Command):
    def __init__(self):
        # Define custom command info here
        # command_keyword = what chat keyword will trigger this command to execute
        # help_message = what message is returned when user sends 'help' message
        # card = optionally send an AdaptiveCard response
        super().__init__(
            command_keyword="admin guide" or "guide" or "Admin guide",
            help_message="Syntax: admin guide devicetype",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # By default, command keyword will be stripped out before being passed to execute function
        # For example, If user sends "weather 12345", then message variable will be " 12345"
        # Need to strip the additional whitespace around the input:
        admin_link=[]
        valid_input=str(message)
        ptrn = r'([aA-zZ]{2}\d{2,3})|([r,c][aA-zZ]{3,12}.\d{2})|((roomkit).{0,5})'
        match=re.search(ptrn, valid_input)
        while match!= None:
            try:
                vc_unit=match.group()
            except:
                print("Unable to match")
            break
        url='https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-maintenance-guides-list.html'

        if vc_unit.upper() == 'ROOM 70' or 'ROOM 55':
            URLAccess.urlaccessed(url)
            regx=re.compile(".+desk-room-board.+")
            default_rm_lnk=sorted(set(list(filter(regx.match, linkcontent))))
            regx2=re.compile(".+room-55d-70-administrator.+")
            unitlink=sorted(set(list(filter(regx2.match, linkcontent))))
            final_link= default_rm_lnk + unitlink
            for endlinks in final_link:
                admin_link.append(endlinks)
            tshootlink=admin_link
        else:
            tshootlink= f"something is not write"
        
        response_message= ("Links for {devc} admin guides are below: \n {endl}".format(devc=vc_unit,endl='\n'.join(tshootlink)))

        # Define our URL, with desired parameters: ZIP code, units, and API Key
        # Message returned will be sent back to the user by bot
        return response_message