import configparser
import os
import sys
dir_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
init_file = os.path.join(os.path.join(dir_folder, 'config'), 'config.ini')
print(init_file)
config = configparser.RawConfigParser()
config.read(init_file)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
