from curses.panel import update_panels
import logging
import requests
from webex_bot.models.command import Command
import re
import os
#from Troubleshooting import*

log = logging.getLogger(__name__)

# Get a free account at openweathermap.org &
# insert API key here:
issue_file=''
location='/home/abhish/snap/code/Test_scripts/Tshoot_info/'

#TP=TroubleshootingTPIssues

class Tshoot(Command):
    def __init__(self):
        # Define custom command info here
        # command_keyword = what chat keyword will trigger this command to execute
        # help_message = what message is returned when user sends 'help' message
        # card = optionally send an AdaptiveCard response
        super().__init__(
            command_keyword="display" or "Display",
            help_message="command syntax: devicetype KW symptom",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # By default, command keyword will be stripped out before being passed to execute function

        valid_input=str(message)
        tshoot_steps=[]
        # Need to strip the additional whitespace around the input:
        ptrn = r'([aA-zZ]{2}\d{2,3})'
        match=re.search(ptrn, valid_input)
        while match!= None:
            try:
                vc_unit=match.group()
            except:
                print("Unable to match")
            break
        #print("is this correct that display issue and unit is {vc}".format(vc=vc_unit))

        if vc_unit.upper() == 'DX80':
            issue_file=os.path.join(location,'DX_80_unresponsivetouch.txt')
            with open(issue_file,'r') as dx80_touchissue:
                for line in dx80_touchissue:
                    tshoot_steps.append(line)
                final_lst=tshoot_steps
        elif vc_unit.upper() == 'MX700' or 'MX800':
            issue_file=os.path.join(location,'MX_series_display_troubleshooting.txt')
            with open(issue_file,'r') as mxseriestshoot:
                for line in mxseriestshoot:
                    tshoot_steps.append(line)
                final_lst=tshoot_steps
        else:
            tshoot_steps="something is not right"
            
        response_message= ("You are facing display issue with {devc}, follow steps below: \n {detail_steps}".format(devc=vc_unit,detail_steps=''.join(final_lst)))
        # Message returned will be sent back to the user by bot
        return response_message
