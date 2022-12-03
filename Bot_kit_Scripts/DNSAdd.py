import json
import logging
import requests
from webex_bot.models.command import Command
import re
import paramiko

log = logging.getLogger(__name__)

#Defining login credentials and destination
dict_creds_host={
    'hostname':'hostname/ip',
    'username':'username',
    'password':'password'
}

class DNSAdd(Command):
    def __init__(self):
        # Define custom command info here
        # command_keyword = what chat keyword will trigger this command to execute
        # help_message = what message is returned when user sends 'help' message
        # card = optionally send an AdaptiveCard response
        super().__init__(
            command_keyword="domain update" or "domain update",
            help_message="Syntax: dns add 'fqdn' 'ip'",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        valid_input=str(message)
        ptrn1 = r'(\w{3,4}([e,c]\w{2}|[p,s,u,b]{1,3}\w{2})(\w{2,9})\d?)'
        ptrn2= r'(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})'
        match=re.search(ptrn1, valid_input)
        match2=re.search(ptrn2,valid_input)
        while (match!= None) and (match2!= None):
            try:
                hostad=match.group()
                ip=match2.group()
                break
            except:
                print("Unable to match")
                break

        cmd = 'powershell Add-DnsServerResourceRecordA -Name "{FQDN}" -ZoneName "uclab.local" -AllowUpdateAny -IPv4Address "{IP_address}" -CreatePtr -TimeToLive 01:00:00'.format(FQDN=hostad,IP_address=ip)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(dict_creds_host['hostname'],username=dict_creds_host['username'],password=dict_creds_host['password'])
        except paramiko.AuthenticationException:
            print("Failed to connect to %s due to wrong username/password" %dict_creds_host['hostname'])
            exit(1)
        except Exception as e:
            print(e.message)    
            exit(2)

        try:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            err = ''.join(stderr.readlines())
            out = ''.join(stdout.readlines())
            final_output = ''
            if (out=='') and (err==''):
                final_output="DNS Entry Added as {FQDN}.uclab.local againts {IPV4}".format(FQDN=hostad,IPV4=ip)
            else:
                final_output=str(out)+str(err)
            print(final_output)
        except Exception as e:
            print(e.message)
        return final_output
