import configparser

config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')


class readConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def getUserEmail():
        e_mail = config.get('common info', 'e_mail')
        return e_mail

    @staticmethod
    def getSearchedText():
        text = config.get('common info', 'search_engine_text')
        return text

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getMessage():
        message = config.get('common info', 'message')
        return message
