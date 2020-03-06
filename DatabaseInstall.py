import configparser
import UpdateServer
import RunInstaller

def runSubProcess(configfile):
    UpdateServer.initialSetup(configfile)
    RunInstaller.installDbSoftware(configfile)

if __name__ == "__main__":
    print("Executed when invoked directly")
    configfile = dict()
    config = configparser.RawConfigParser()

    try:
        config.read('config.ini')
        configfile["19c"] = config.get("INSTALLCOMMAND", "PREINSTALL19C")
        configfile["parentdir"] = config.get("INSTALLCOMMAND", "MOUNTPOINTDB")
        configfile["owner"] = config.get("INSTALLCOMMAND", "OWNER")
        configfile["base"] = config.get("DEFAULT", "ORACLEBASE")
        configfile["oraInv"] = config.get("DEFAULT", "ORACLEINV")
        configfile["hostname"] = config.get("DEFAULT", "HOSTNAME")

        if(config.get("DEFAULT","ORACLEHOME19c") != ""):
            configfile["oraclehome"] = config.get("DEFAULT", "ORACLEHOME19c")
            configfile["zip"] = config.get("ZIPFILES", "19c")
            configfile["software"] = config.get("INSTALLCOMMAND", "PREINSTALL19C")
            runSubProcess(configfile)
        if(config.get("DEFAULT","ORACLEHOME18c") != "" ):
            print('con')
        if(config.get("DEFAULT","ORACLEHOME12.2c") != "" ):
            configfile["oraclehome"] = config.get("DEFAULT", "ORACLEHOME12.2c")
            configfile["zip"] = config.get("ZIPFILES", "12.2c")
            configfile["software"] = config.get("INSTALLCOMMAND", "PREINSTALL12.2c")
            runSubProcess(configfile)
        if(config.get("DEFAULT","ORACLEHOME12.1c") != "" ):
            print('con')
        if(config.get("DEFAULT","ORACLEHOME11g") != "" ):
            print('con')


    except BaseException as err :
        print(err)
        exit(1)


else:
    print("Executed when imported")
