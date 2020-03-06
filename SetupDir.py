import os
import subprocess


def setPremissions(config):
    process = subprocess.Popen(['sudo', 'su', '-'], universal_newlines=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write("mkdir -p " + config["oraclehome"] + ";")
    process.stdin.write("chown -R " + config["owner"]+ " " + config["parentdir"] +"; " + "chmod 775 -R " + config["parentdir"] + ";" )
    process.stdin.close()
    for line in process.stdout:
        print(line)
    for line in process.stderr:
        print(line + " error")
    print(str(process.wait()) + " wait3")

if __name__ == "__main__":
    setPremissions(config)

