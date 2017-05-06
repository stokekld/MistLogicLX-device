import os

class deviceTrigger(object):

    def __init__(self, state):
        self.state = state
        self.__change()

    def __change(self):
        if self.state['manual']:
            os.system("echo 1 > /sys/class/gpio/gpio23/value")
        else:
            os.system("echo 0 > /sys/class/gpio/gpio23/value")

