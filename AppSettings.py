import os

class AppSettings:
    def getAppSetting(self, key):
        settings = self.readSettings()

        if key in settings:
            return settings[key]

        return ''

    def setAppSetting(self, key, value):
        settings = self.readSettings()
        settings[key] = value
        self.writeSettings(settings)

    def readSettings(self):
        settings = {}
        fileName = self.getSettingsFilename()

        if not os.path.exists(fileName):
            return settings

        file=open(fileName)
        for line in file:
            split = line.split('=',1)
            if len(split) < 2:
                continue

            key = split[0]
            value = split[1].strip()
            settings[key]=value
        file.close()

        return settings 

    def writeSettings(self, settings):
        file=open(self.getSettingsFilename(), 'w')
        for key in settings:
            line = key + '=' + settings[key] + '\n'
            file.write(line)
        file.close()

    def getSettingsFilename(self):
        path = os.path.dirname(__file__)
        return os.path.join(path, 'settings.txt')


if __name__ == '__main__':
    settings = AppSettings()
    value = settings.getAppSetting('Test')
    print(value)
    settings.setAppSetting('Test', 'Value')
