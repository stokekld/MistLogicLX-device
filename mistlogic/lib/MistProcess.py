from subprocess import check_output
from MistSys import commandExe
from MistError import Error, Info
import os, signal


class Process(object):
    def getPid(self, name):
        try:
            return int(commandExe("pidof %s" % name).output)
        except:
            Info("No se encontro el pid de %s" % name)
            return 0

    def killByName(self, name):

        pid = self.getPid(name)

        if pid is 0:
            return False

        try:
            os.kill(pid, signal.SIGKILL)
            return True
        except Exception as e:
            raise Error(e.message)

