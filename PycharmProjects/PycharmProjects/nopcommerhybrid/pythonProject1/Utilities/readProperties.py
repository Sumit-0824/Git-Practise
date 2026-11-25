import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        URL=config.get('common info','baseURL')
        return URL

    @staticmethod
    def getusername():
        URL = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        URL = config.get('common info', 'password')
        return password