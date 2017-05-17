import sys, os
os.environ["MAIN_DIR"] = os.path.dirname(os.path.abspath(__file__))
libPath = os.path.join(os.environ["MAIN_DIR"], '../lib')
sys.path.append(libPath)

import RPi.GPIO as GPIO
from Mist.app import service
from MistDB import dbDevice

device = dbDevice()

if device.getProp('manual'):
    manualInit = GPIO.HIGH
else:
    manualInit = GPIO.LOW

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.OUT, initial=manualInit)

service.run(host=service.config['HOST'], port=service.config['PORT'], debug=service.config['DEBUG'])
