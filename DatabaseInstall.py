import configparser
import os
import subprocess
import SetEnv
import SetupDir
import UpdateServer
import RunInstaller

def runSubProcess(configfile):
    UpdateServer.initialSetup(configfile)
    RunInstaller.installDbSoftware(configfile)

def readConfigFile():
    configs = configparser.RawConfigParser()
    configs.read('config.ini')

if __name__ == "__main__":
    print("Executed when invoked directly")
    yumconfig = dict()
    config = configparser.RawConfigParser()
    try:
        config.read('config.ini')
        yumconfig["update"] = config.get("INSTALLCOMMAND", "UPDATE")
        yumconfig["19c"] = config.get("INSTALLCOMMAND", "PREINSTALL19C")
        yumconfig["oraclehome"] = config.get("DEFAULT","ORACLEHOME")
        yumconfig["parentdir"] = config.get("INSTALLCOMMAND", "DIRP")
        yumconfig["owner"] = config.get("INSTALLCOMMAND", "OWNER")
        yumconfig["base"] = config.get("DEFAULT", "ORACLEBASE")
        yumconfig["zip"] = config.get("ZIPFILES", "19c")
        yumconfig["oraInv"] = config.get("DEFAULT", "ORACLEINV")
        yumconfig["hostname"] = config.get("DEFAULT", "HOSTNAME")
    except BaseException:
        print("Something when wrong with your config file.")
        exit(1)

    print(yumconfig)
    runSubProcess(yumconfig)
    os.getlogin()

else:
    print("Executed when imported")