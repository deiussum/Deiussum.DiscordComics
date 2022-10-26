import os
import requests
import AppSettings
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class PennyArcadeBot:
    def __init__(self):
        self.url = 'https://www.penny-arcade.com/comic'
        self.discordHook = os.environ['PENNY_HOOK']
        self.appSettings = AppSettings.AppSettings()

    def postLatest(self):
        current = self.getCurrent()

        if self.isNewComic(current):
            self.postToDiscord(current)

    def postToDiscord(self, current):
        msg = f"{current['title']}\r\n{current['img']}"

        requests.post(self.discordHook, data={'content': msg} )

        self.appSettings.setAppSetting('LAST_PENNY', current['img'])

    def getCurrent(self):
        result = requests.get(self.url)
        html = pq(result.text)

        return {
            'title': html("meta[property='og:title']").attr['content'],
            'img': html("meta[property='og:image']").attr['content']
        }

    def isNewComic(self, current):
        lastComic = self.appSettings.getAppSetting('LAST_PENNY')
        return lastComic != current['img']


if __name__ == '__main__':
    load_dotenv()
    x = PennyArcadeBot()
    x.postLatest()

