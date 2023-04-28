import os
import requests
import AppSettings
from Environment import Environment as env 
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class PennyArcadeBot:
    def __init__(self):
        self.url = 'https://www.penny-arcade.com/comic'
        self.discordHooks = env.getEnvVariableAsDictionary('PENNY_HOOK')
        self.appSettings = AppSettings.AppSettings()

    def postLatest(self):
        current = self.getCurrent()

        for key, discordHook in self.discordHooks.items():
            if self.isNewComic(current, key):
                self.postToDiscord(current, discordHook, key)

    def postToDiscord(self, current, discordHook, hookIndex):
        url = current['url']

        requests.post(discordHook, data={'content': url} )

        self.appSettings.setAppSetting('LAST_PENNY' + str(hookIndex), url)

    def getCurrent(self):
        result = requests.get(self.url)
        html = pq(result.text)

        return {
            'title': html("meta[property='og:title']").attr['content'],
            'img': html("meta[property='og:image']").attr['content'],
            'url': html("meta[property='og:url']").attr['content'],
        }

    def isNewComic(self, current, hookIndex):
        lastComic = self.appSettings.getAppSetting('LAST_PENNY' + str(hookIndex))

        return lastComic != current['url']


if __name__ == '__main__':
    load_dotenv()
    x = PennyArcadeBot()
    x.postLatest()

