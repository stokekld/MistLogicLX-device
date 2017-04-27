#!/usr/bin/python

from MistLogic.MistNet import NetConf
from MistLogic.MistControl import Control

config = NetConf().conf

if config['ap']:
    Control().startHostapd()
else:
    Control().startWifiConnect()

