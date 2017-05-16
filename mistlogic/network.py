import sys, os

os.environ["MAIN_DIR"] = os.path.dirname(os.path.abspath(__file__))

libPath = os.path.join(os.environ["MAIN_DIR"], 'lib')
sys.path.append(libPath)

from MistDB import dbNet
from MistControl import Control

netconf = dbNet()

if netconf.getProp('ap'):
    Control().startHostapd()
else:
    Control().startWifiConnect()
