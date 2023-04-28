import os

class Environment:
    def getEnvVariable(variableName):
        return os.environ.get(variableName)

    def getEnvVariableAsDictionary(variableName):
        envVariables = {}

        single = Environment.getEnvVariable(variableName)

        if single != None:
            envVariables[1] = single
        else:
            index = 1
            settingItem = Environment.getEnvVariable(variableName + str(index))
            while settingItem != None:
                envVariables[index] = settingItem
                index += 1
                settingItem = Environment.getEnvVariable(variableName + str(index))
        return envVariables

if __name__ == '__main__':
    valueDict = Environment.getEnvVariableAsDictionary('TEST')
    print(valueDict)
    singleDict = Environment.getEnvVariableAsDictionary('SINGLE_TEST')
    print(singleDict)


