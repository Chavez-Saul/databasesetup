import subprocess

""" Switch user and setup env """
def initialSetup(configfile):
    process = subprocess.Popen(['sudo', 'su', '-'], universal_newlines=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write("yum update -y;")
    process.stdin.write("yum install " + configfile["19c"] + " -y;")
    process.stdin.write("mkdir -p " + configfile["oraclehome"] + ";")
    process.stdin.write("chown -R " + configfile["owner"] + " " +
                        configfile["parentdir"] + "; " + "chmod 775 -R " + configfile["parentdir"] + ";")
    process.stdin.close()

    for line in process.stdout:
        print(line)
    for line in process.stderr:
        print(line + " error")

    process = subprocess.Popen(['sudo', 'su', '-', 'oracle'], universal_newlines=True,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    for line in process.communicate():
        print(line)

