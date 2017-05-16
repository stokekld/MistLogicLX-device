from MistSys import commandExe

class Network(object):

    def __init__(self, iface):
        self.iface = iface

    def ipFlush(self):
        return commandExe('ip addr flush dev %s' % self.iface)

    def setIp(self, ip, netmask, broadcast):
        return commandExe('ip addr add %s/%s brd %s dev %s' % (ip, netmask, broadcast, self.iface))
