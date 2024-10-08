import requests
import AppSettings
from ComicLogger import ComicLogger as log
from Environment import Environment as env 
from pyquery import PyQuery as pq
from dotenv import load_dotenv

class XkcdBot:
    def __init__(self):
        self.url = 'https://xkcd.com'
        self.appSettings = AppSettings.AppSettings()
        self.discordHooks = env.getEnvVariableAsDictionary('XKCD_HOOK')

    def postLatest(self):
        log.info('XkcdBot', 'Checking for new Xkcd')
        current = self.getCurrent()

        for key, discordHook in self.discordHooks.items():
            if self.isNewComic(current, key):
                log.info('XkcdBot', 'New Xkcd comic found')
                self.postToDiscord(current, discordHook, key)


    def postToDiscord(self, current, discordHook, hookIndex):
        url = current['url']

        titleLink = f"[{current['title']}]({url})"
        description = f"||{current['altText']}||"
        imageUrl = current['img']

        msg = f'''
         {{
            "content": "{titleLink}",
            "embeds": [
                {{ 
                    "description": "{description}", 
                    "image": {{ 
                        "url": "{imageUrl}" 
                    }} 
                }}
            ]
        }}
        '''

        #print(msg)

        response = requests.post(discordHook, msg, headers={'Content-Type': 'application/json'})
        #print(response.reason)
        #print(response.text)

        self.appSettings.setAppSetting('LAST_XKCD' + str(hookIndex), url)

    
    def getCurrent(self):
        result = requests.get(self.url)
        html = pq(result.text)
        img = f"https:{html('#comic img').attr['src']}"
        url = html("meta[property='og:url']").attr['content']

        return {
            'title':  html('#ctitle').html().replace('"', '\\"'),
            'img':  img,
            'altText': html('#comic img').attr['title'].replace('"', '\\"'),
            # Sometimes the metadata tag is empty for the url.  Fall back to the img tag when that happens
            'url': url or img 
        }

    def isNewComic(self, current, index):
        lastComic = self.appSettings.getAppSetting('LAST_XKCD' + str(index))
        return lastComic != current['url']



if __name__ == '__main__':
    log.initialize()
    load_dotenv()
    x = XkcdBot()
    x.postLatest()

