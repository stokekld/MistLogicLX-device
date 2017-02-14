from . import MAIN_DIR, commandExe
import MistLogic, json, os, signal

class NetConf(object):

    file = 'netconf.json'
    path_file = os.path.join(MAIN_DIR, file)
    conf = {'ap':True, 'dhcp':False, 'ip':'192.168.1.1', 'netmask':'255.255.255.0'}

    def __init__(self):
        self.load()

    def load(self):
        try:
            with open(self.path_file) as netconf:
                self.conf = json.load(netconf)
        except (IOError, ValueError) as e:
            self.store()

    def store(self):
	with open(self.path_file, 'w') as netconf:
            json.dump(self.conf, netconf)

    def exist(self, key):
        if key in self.conf:
            return True
        return False

    def get(self, key):
        if self.exist(key):
            return self.conf[key]

    def set(self, key, value):
        if self.exist(key):
            self.conf[key] = value
            self.store()
            return True
        return False

class Network(object):

    def __init__(self, iface):
        self.iface = iface

    def ipFlush(self):
        return commandExe('ip addr flush dev %s' % self.iface)

    def setIp(self, ip, netmask):
        return commandExe('ip addr add %s/%s dev %s' % (ip, netmask, self.iface))
