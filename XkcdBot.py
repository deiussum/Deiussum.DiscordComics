import os
import requests
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class XkcdBot:
    def postLatest(self):
        result = requests.get("https://xkcd.com")

        html = pq(result.text)
        title = html("#ctitle").html()
        src = "https:" + html("#comic img").attr["src"]
        altText = "Alt text: " + html("#comic img").attr["title"]

        discordHook = os.environ["XKCD_HOOK"]

        msg = title + "\r\n" + src
        #print(msg)
        requests.post(discordHook, data={'content': msg} )
        requests.post(discordHook, data={'content': altText} )

load_dotenv()
x = XkcdBot()
x.postLatest()

