from subprocess import check_output
import os, signal

class Process(object):
    def getPid(self, name):
        try:
            return check_output(["pidof", name])
        except:
            return 0

    def killByPid(self, pid):
        try:
            os.kill(pid, signal.SIGKILL)
            return True
        except:
            return False
