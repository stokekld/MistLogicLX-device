from MistProcess import Process
from MistNet import Network
from MistTools import Tools
from MistDB import dbNet

class Control(object):

    interface = "wlan0"
    hostapconf = "/etc/mistlogic/hostapd.conf"

    def __init__(self):
        self.process = Process()
        self.network = Network(self.interface)
        self.tools = Tools(self.interface)
        self.netconf = dbNet()

    def killProcess(self):
        self.process.killByName('dhcpd')
        self.process.killByName('dhclient')
        self.process.killByName('hostapd')
        self.process.killByName('wpa_supplicant')

    def startHostapd(self):
        self.killProcess()
        self.network.ipFlush()
        self.network.setIp("192.168.1.1", "24", "192.168.1.255")
        self.tools.hostapdStart(self.hostapconf)
        self.tools.dhcpServer()

    def startWifiConnect(self):
        self.killProcess()
        self.network.ipFlush()
        self.tools.wpaPassphrase(self.netconf.getProp("ssid"), self.netconf.getProp("passphrase"))
        self.tools.wpaConnect()
        if self.netconf.conf['dhcp']:
            self.tools.dhcpClient()

        
