from Scraper import *
import re
class AdminGuide_Main:
    def __init__(self,devices):
        self.devices=devices
        self.admin_link=[]
    
    def adminguides(self, codec_ing, url):
        URLAccess.urlaccessed(url)
        regx=re.compile(codec_ing)
        unitlink=sorted(set(list(filter(regx.match, linkcontent))))
        for endlinks in unitlink:
            self.admin_link.append(endlinks)
        tshootlink=self.admin_link
        return tshootlink
        

    def curated_guide(self):
        url='https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-maintenance-guides-list.html'
        try:
            if self.devices == 'ROOM 70D' or self.devices=='ROOM 55D':
                codec_ing=".+room-55d-70-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices == 'ROOM 70':
                codec_ing=".+room-70g2-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices == 'ROOM 55':
                codec_ing=".+room-55-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices == 'ROOMKIT':
                codec_ing=".+room-kit-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices == 'ROOMKIT MINI':
                codec_ing=".+room-kit-mini-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices == 'ROOMKIT PLUS':
                codec_ing=".+codec-plus-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices == 'ROOMKIT PRO':
                codec_ing=".+codec-pro-administrator.+"
                guides=self.adminguides(codec_ing,url)
            elif self.devices =='ROOMOS':
                codec_ing=".+desk-room-board.+"
                guides=self.adminguides(codec_ing,url)
        except ValueError:
            guides='404 Not found'

        return guides
