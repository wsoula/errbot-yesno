from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
import json
import requests

class Yesno(BotPlugin):
    """Returns gif from http://yesno.wtf/api"""

    @botcmd
    def yesno(self,msg,args):
        url='http://yesno.wtf/api'
        page = urllib.request.Request(url)
        response = json.loads(urllib.request.urlopen(page).read().decode('utf-8'))
        image_url = response['image']
        image_bytes = requests.get(image_url).content
        file = open('tmp.gif','wb')
        file.write(image_bytes)
        file.close()
        self.send_stream_request(msg.frm,open('tmp.gif','rb'), name='image.gif', stream_type='image/gif')
