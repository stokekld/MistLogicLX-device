MAIN_DIR = '..'


def commandExe(self, command):
    try:
        os.system(command)
        return True
    except:
        return False
