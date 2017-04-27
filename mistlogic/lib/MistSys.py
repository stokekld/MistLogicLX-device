from .MistError import Error, Info
import subprocess

class commandExe:

    output = ""
    command = ""

    def __init__(self, command):
        self.command = command
        self.execute()

    def execute(self):
        try:
            Info('Ejecutando %s' % self.command)
            self.output = subprocess.check_output(self.command, shell=True, stderr=subprocess.STDOUT)
            Info(self.output)
            return True
        except Exception as e:
            Info('Error al tratar de ejecutar el comando %s' % self.command)
            raise Error(e.message)
            return False
