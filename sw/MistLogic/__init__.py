MAIN_DIR = '..'


def commandExe(command):
    try:
        os.system(command)
        return True
    except:
        return False
