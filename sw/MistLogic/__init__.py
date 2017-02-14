MAIN_DIR = '..'


def commandExe(command):
    try:
        os.system(command)
        return True
    except Exception as e:
        print e.message, e.args
        return False
