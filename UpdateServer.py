#This will be run on thread 1
import subprocess


def yumUpdate(configfile):
    process = subprocess.Popen(['sudo', 'su', '-'], universal_newlines=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write("yum " + configfile["update"] +" -y;")
    process.stdin.write("yum install " + configfile["19c"] + " -y;")
    process.stdin.close()
    for line in process.stdout:
        print(line)
    for line in process.stderr:
        print(line + " error")
    print(str(process.wait()) + " wait3")
    process = subprocess.Popen(['sudo', 'su', '-', 'oracle'], universal_newlines=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write('whoami')
    # process.stdin.close()
    for line in process.communicate():
        print(line)

if __name__ == "__main__":
    yumUpdate(configfile)


