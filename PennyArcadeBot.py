import os
import requests
import AppSettings
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

        appSettings = AppSettings.AppSettings()
        lastComic = appSettings.GetAppSetting('LAST_PENNY')
        if lastComic != img:
            requests.post(discordHook, data={'content': msg} )
            appSettings.SetAppSetting('LAST_PENNY', img)

load_dotenv()
x = XkcdBot()
x.postLatest()

