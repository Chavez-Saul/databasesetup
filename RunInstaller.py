import subprocess

def installDbSoftware(config):
    process = subprocess.Popen(['sudo', 'su', '-', 'oracle'], universal_newlines=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write("export ORACLE_BASE=" + config["base"] + "; "
                        + "export ORA_INVENTORY=" + config["oraInv"] +"; "
                        + "export ORACLE_HOSTNAME="
                        + config["hostname"] + "; env;")

    if(config["oraclehome"] == "/u01/app/oracle/product/19.3.0.0/dbhome_1"):
        process.stdin.write("export ORACLE_HOME=" + config["oraclehome"] +";cd $ORACLE_HOME;")
        process.stdin.write("unzip " + config["zip"] + "; ")
        process.stdin.write("""./runInstaller -ignorePrereq -waitforcompletion -silent \\
        -responseFile ${ORACLE_HOME}/install/response/db_install.rsp \\
        oracle.install.option=INSTALL_DB_SWONLY\\
        ORACLE_HOSTNAME=${ORACLE_HOSTNAME}\\
        UNIX_GROUP_NAME=oinstall\\
        INVENTORY_LOCATION=${ORA_INVENTORY}\\
        SELECTED_LANGUAGES=en,en_GB\\
        ORACLE_HOME=${ORACLE_HOME}\\
        ORACLE_BASE=${ORACLE_BASE}\\
        oracle.install.db.InstallEdition=EE\\
        oracle.install.db.OSDBA_GROUP=dba\\
        oracle.install.db.OSBACKUPDBA_GROUP=dba\\
        oracle.install.db.OSDGDBA_GROUP=dba\\
        oracle.install.db.OSKMDBA_GROUP=dba\\
        oracle.install.db.OSRACDBA_GROUP=dba\\
        SECURITY_UPDATES_VIA_MYORACLESUPPORT=false\\
        DECLINE_SECURITY_UPDATES=true;""")

    elif(config["oraclehome"] == "/u01/app/oracle/product/12.2.0.1/dbhome_1"):
        process.stdin.write("export ORACLE_HOME=" + config["oraclehome"] +";cd /tmp;pwd;")
        process.stdin.write("unzip " + config["zip"] + "; ")
        process.stdin.write("""/tmp/database/runInstaller -ignorePrereq -waitforcompletion -silent \\
        -responseFile /tmp/database/response/db_install.rsp \\
        oracle.install.option=INSTALL_DB_SWONLY\\
        ORACLE_HOSTNAME=${ORACLE_HOSTNAME}\\
        UNIX_GROUP_NAME=oinstall\\
        INVENTORY_LOCATION=${ORA_INVENTORY}\\
        SELECTED_LANGUAGES=en,en_GB\\
        ORACLE_HOME=${ORACLE_HOME}\\
        ORACLE_BASE=${ORACLE_BASE}\\
        oracle.install.db.InstallEdition=EE\\
        oracle.install.db.OSDBA_GROUP=dba\\
        oracle.install.db.OSBACKUPDBA_GROUP=dba\\
        oracle.install.db.OSDGDBA_GROUP=dba\\
        oracle.install.db.OSKMDBA_GROUP=dba\\
        oracle.install.db.OSRACDBA_GROUP=dba\\
        SECURITY_UPDATES_VIA_MYORACLESUPPORT=false\\
        DECLINE_SECURITY_UPDATES=true;""")
    process.stdin.close()


    for line in process.stdout:
        print(line)

    for line in process.stderr:
        print(line + " error")


