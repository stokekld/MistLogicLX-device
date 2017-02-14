import os

class Tools(object):

    def __init__(self, iface)
        self.iface = iface

    def commandExe(self, command):
        try:
            os.system(command)
            return True
        except:
            return False

    def wpaConnect(self, ssid, passphrase):
        return commandExe('wpa_supplicant -B -i %s -Dwext -c <(wpa_passphrase %s %s)' % (self.iface, ssid, passphrase))

    def hostapdStart(self, fileConf):
        return commandExe('hostapd -B %s' % fileConf)

    def dhcpClient(self):
        return commandExe('dhclient %s' % self.iface)

    def dhcpServer(self):
        return commandExe('dhcpd %s' % self.iface)
