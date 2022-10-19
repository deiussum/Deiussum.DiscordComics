from os.path import exists

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

        if not exists(fileName):
            return settings

        file=open(fileName)
        for line in file:
            print(line)
            split = line.split('=',1)
            key = split[0]
            print(key)
            value = split[1]
            print(value)
            settings[key]=value
        file.close()

        return settings 

    def WriteSettings(self, settings):
        file=open(self.GetSettingsFilename(), "w")
        for key in settings:
            line = key + '=' + settings[key] + '\r\n'
            file.write(line)
        file.close()

    def GetSettingsFilename(self):
        return "settings.txt"


if __name__ == '__main__':
    settings = AppSettings()
    value = settings.GetAppSetting('Test')
    print(value)
    settings.SetAppSetting('Test', 'Value')
