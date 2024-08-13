import configparser
import os

def parseConfigFile() -> dict:
    #check if there is a config file
    if not os.path.exists(os.getcwd() + "/poc/settings.conf"):
        raise FileExistsError()

    config = configparser.ConfigParser()
    config.read(os.getcwd() + "/poc/settings.conf")

    return config