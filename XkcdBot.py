import os
import requests
import AppSettings
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class XkcdBot:
    def __init__(self):
        self.url = 'https://xkcd.com'
        self.appSettings = AppSettings.AppSettings()
        self.discordHook = os.environ['XKCD_HOOK']

    def postLatest(self):
        current = self.getCurrent()

        if self.isNewComic(current):
            self.postToDiscord(current)


    def postToDiscord(self, current):
        msg = f"{current['title']}\r\n{current['img']}"

        requests.post(self.discordHook, data={'content': msg} )
        requests.post(self.discordHook, data={'content': current['altText']} )

        self.appSettings.setAppSetting('LAST_XKCD', current['img'])

    
    def getCurrent(self):
        result = requests.get(self.url)
        html = pq(result.text)

        return {
            'title':  html('#ctitle').html(),
            'img':  f"https:{html('#comic img').attr['src']}",
            'altText': f"Alt text: {html('#comic img').attr['title']}"
        }

    def isNewComic(self, current):
        lastComic = self.appSettings.getAppSetting('LAST_XKCD')
        return lastComic != current['img']



if __name__ == '__main__':
    load_dotenv()
    x = XkcdBot()
    x.postLatest()

