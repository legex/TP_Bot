import requests
from bs4 import BeautifulSoup
from datetime import*
import re
import sslbypass

linkcontent=[]

class URLAccess():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def urlaccessed(url):
        req=sslbypass.get_legacy_session().get(url)
        ur=req.text
        soup=BeautifulSoup(ur,'html.parser')
        for link in soup.find_all('a', attrs={'href': re.compile('^/c/dam/en/us/td/docs/')}):
            activelinks= 'https://www.cisco.com'+(link.get('href'))
            linkcontent.append(activelinks)
        return linkcontent