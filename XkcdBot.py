import os
import requests
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class XkcdBot:
    def postLatest(self):
        result = requests.get("https://xkcd.com")

        html = pq(result.text)
        src = "https:" + html("#comic img").attr["src"]
        title = "Alt text: " + html("#comic img").attr["title"]

        discordHook = os.environ["XKCD_HOOK"]

        #print(msg)
        requests.post(discordHook, data={'content': src} )
        requests.post(discordHook, data={'content': title} )

load_dotenv()
x = XkcdBot()
x.postLatest()

