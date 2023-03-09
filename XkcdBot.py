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
        url = current['url']

        msg = f"{current['title']}\n||{current['altText']}||\n{current['img']}"

        requests.post(self.discordHook, data={'content': msg} )

        self.appSettings.setAppSetting('LAST_XKCD', url)

    
    def getCurrent(self):
        result = requests.get(self.url)
        html = pq(result.text)

        return {
            'title':  html('#ctitle').html(),
            'img':  f"https:{html('#comic img').attr['src']}",
            'altText': f"Alt text: {html('#comic img').attr['title']}",
            'url': html("meta[property='og:url']").attr['content'],
        }

    def isNewComic(self, current):
        lastComic = self.appSettings.getAppSetting('LAST_XKCD')
        return lastComic != current['url']



if __name__ == '__main__':
    load_dotenv()
    x = XkcdBot()
    x.postLatest()

