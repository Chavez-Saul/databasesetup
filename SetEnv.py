import os
import subprocess

def setEnvforOracle(config):
    process = subprocess.Popen(['sudo', 'su', '-', 'oracle'], universal_newlines=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write("export ORACLE_HOME=" + config["oraclehome"] + "; " "export ORACLE_BASE=" + config["base"] + "; ")
    process.stdin.write("cd $ORACLE_HOME;")
    process.stdin.write("unzip " + config["zip"] + "; ")
    process.stdin.close()
    for lin in process.stdout:
        print(lin + " setevn")

    print(str(os.getlogin()) + " this is the current user")

if __name__ == "__main__":
    setEnvforOracle(config)
