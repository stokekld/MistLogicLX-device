from .MistProcess import Process
from .MistNet import Network, NetConf
from .MistTools import Tools

class Control(object):

    interface = "wlan0"
    hostapconf = "/etc/hostapd/hostapd.conf"

    def __init__(self):
        self.process = Process()
        self.network = Network(self.interface)
        self.tools = Tools(self.interface)
        self.netconf = NetConf()

    def killProcess(self):
        self.process.killByName('dhcpd')
        self.process.killByName('dhclient')
        self.process.killByName('hostapd')
        self.process.killByName('wpa_supplicant')

    def startHostapd(self):
        self.killProcess()
        self.network.ipFlush()
        self.network.setIp("192.168.1.1", "24")
        self.tools.hostapdStart(self.hostapconf)
        self.tools.dhcpServer()

    def startWifiConnect(self):
        self.killProcess()
        self.network.ipFlush()
        self.tools.wpaPassphrase(self.netconf.get("ssid"), self.netconf.get("passphrase"))
        self.tools.wpaConnect()
        if self.netconf.conf['dhcp']:
            self.tools.dhcpClient()
        # print self.netconf.get("passphrase")

        
