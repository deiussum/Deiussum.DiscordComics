import os

class AppSettings:
    def GetAppSetting(self, key):
        settings = self.ReadSettings()

        if key in settings:
            return settings[key]

        return ''

    def SetAppSetting(self, key, value):
        settings = self.ReadSettings()
        settings[key] = value
        self.WriteSettings(settings)

    def ReadSettings(self):
        settings = {}
        fileName = self.GetSettingsFilename()

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

    def WriteSettings(self, settings):
        file=open(self.GetSettingsFilename(), "w")
        for key in settings:
            line = key + '=' + settings[key] + '\n'
            file.write(line)
        file.close()

    def GetSettingsFilename(self):
        path = os.path.dirname(__file__)
        return os.path.join(path, "settings.txt")


if __name__ == '__main__':
    settings = AppSettings()
    value = settings.GetAppSetting('Test')
    print(value)
    settings.SetAppSetting('Test', 'Value')
