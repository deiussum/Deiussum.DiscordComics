import os
import requests
import AppSettings
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
        appSettings = AppSettings.AppSettings()
        lastComic = appSettings.GetAppSetting('LAST_XKCD')

        if lastComic != src:
            requests.post(discordHook, data={'content': msg} )
            requests.post(discordHook, data={'content': altText} )
            appSettings.SetAppSetting('LAST_XKCD', src)

load_dotenv()
x = XkcdBot()
x.postLatest()

