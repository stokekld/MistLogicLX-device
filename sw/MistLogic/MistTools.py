from .MistSys import commandExe
import os

class Tools(object):

    wpaConfPath = '/etc/wpa_supplicant/wpa_supplicant.conf'

    def __init__(self, iface):
        self.iface = iface

    def wpaPassphrase(self, ssid, passphrase):
        f = open(self.wpaConfPath, 'w')
        f.write('network={{\n    ssid="{}"\n    psk="{}"\n}}\n'.format(
            ssid, passphrase))
        f.close()
        # return commandExe('wpa_passphrase "%s" "%s" > %s' % (ssid, passphrase, self.wpaConfPath)).success

    def wpaConnect(self):
        return commandExe('wpa_supplicant -B -i %s -Dwext -c /etc/wpa_supplicant/wpa_supplicant.conf' % self.iface)

    def hostapdStart(self, fileConf):
        return commandExe('hostapd -B %s' % fileConf)

    def dhcpClient(self):
        return commandExe('dhclient %s' % self.iface)

    def dhcpServer(self):
        return commandExe('dhcpd %s' % self.iface)
