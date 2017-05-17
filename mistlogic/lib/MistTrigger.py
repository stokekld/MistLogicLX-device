import os
import RPi.GPIO as GPIO

class deviceTrigger(object):

    def __init__(self, state):
        self.state = state
        self.__change()

    def __change(self):
        if self.state['manual']:
            GPIO.output(23, GPIO.HIGH)
        else:
            GPIO.output(23, GPIO.LOW)

