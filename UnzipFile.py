import zipfile

def unzipFiles():
    zipfile.ZipFile('/home/opc/LINUX.X64_193000_db_home.zip').extractall()

if __name__ == "__main__":
    unzipFiles()

