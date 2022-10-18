import os
import requests
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class XkcdBot:
    def postLatest(self):
        result = requests.get("https://www.penny-arcade.com/comic")
        # print(result.text)

        html = pq(result.text)
        title = html("meta[property='og:title']").attr["content"]
        img = html("meta[property='og:image']").attr["content"]

        discordHook = os.environ["PENNY_HOOK"]

        msg = title + "\r\n" + img
        # print(msg)

        requests.post(discordHook, data={'content': msg} )

load_dotenv()
x = XkcdBot()
x.postLatest()

