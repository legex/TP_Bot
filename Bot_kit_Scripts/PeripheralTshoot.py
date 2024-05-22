import logging
import requests
from webex_bot.models.command import Command
import os
import re
#from Troubleshooting import*

log = logging.getLogger(__name__)

issue_file=''
location='/home/abhish/snap/code/Test_scripts/Tshoot_info/'
var_issue=''
#TP=TroubleshootingTPIssues

class Peripherals(Command):
    def __init__(self):
        # Define custom command info here
        # command_keyword = what chat keyword will trigger this command to execute
        # help_message = what message is returned when user sends 'help' message
        # card = optionally send an AdaptiveCard response
        super().__init__(
            command_keyword="peripheral" or "Peripheral",
            help_message="command syntax: peripheral issue unit or  peripheral device unit",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # By default, command keyword will be stripped out before being passed to execute function
        valid_input=str(message)
        tshoot_steps=[]

        ptrn = r'([t,s,p,q,r,w][aA-zZ]{0,14}\d{0,2}$)'                # Regex pattern to match hardware devices
        match=re.search(ptrn, valid_input)
        while match!= None:
            try:
                vc_unit=match.group(1)
            except:
                print("Unable to match")
            break

        if vc_unit.upper() == 'TOUCH10' or 'WEBEX NAVIGATOR' or 'TOUCH 10' or 'WEBEXNAVIGATOR':
            issue_file=os.path.join(location,'Touchpanel_tshoot.txt')
            with open(issue_file,'r') as touchpanel:
                for line in touchpanel:
                    tshoot_steps.append(line)
                final_lst=tshoot_steps
        elif var_issue== 'issue' or var_issue== 'left' or vc_unit== 'mx800/700' or var_issue== 'left display':
            issue_file=os.path.join(location,'MX_series_display_troubleshooting.txt')
            with open(issue_file,'r') as dx80_touchissue:
                for line in dx80_touchissue:
                    tshoot_steps.append(line)
                final_lst=tshoot_steps
        elif var_issue== 'issue' or var_issue== 'touchpanel' or vc_unit== 'touch10' or var_issue== 'Unresponsivetouch':
            issue_file=os.path.join(location,'Touchpanel_tshoot.txt')
            with open(issue_file,'r') as dx80_touchissue:
                for line in dx80_touchissue:
                    tshoot_steps.append(line)
                final_lst=tshoot_steps
        else:
            tshoot_steps="something is not right"
            
        response_message= ("You are facing issue with {devc},follow steps below: \n {detail_steps}".format(devc=vc_unit,detail_steps=''.join(final_lst)))

        # Message returned will be sent back to the user by bot
        return response_message
