# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/login/Servers.py
import BigWorld, Settings
from gui import GUI_SETTINGS
from Event import Event
from predefined_hosts import g_preDefinedHosts, REQUEST_RATE

class Servers(object):
    onServersStatusChanged = Event()

    def __init__(self, loginPreferences):
        self._loginPreferences = loginPreferences
        s = Settings.g_instance
        g_preDefinedHosts.readScriptConfig(s.scriptConfig, s.userPrefs)
        g_preDefinedHosts.onCsisQueryStart += self.__onServerUpdate
        g_preDefinedHosts.onPingPerformed += self.__onServerUpdate
        g_preDefinedHosts.onCsisQueryComplete += self.__onServerUpdate
        if GUI_SETTINGS.csisRequestRate == REQUEST_RATE.ALWAYS:
            g_preDefinedHosts.startCSISUpdate()
        g_preDefinedHosts.requestPing()
        self._serverList = []
        self._selectedServerIdx = 0
        self.updateServerList()

    def fini(self):
        g_preDefinedHosts.stopCSISUpdate()
        g_preDefinedHosts.onCsisQueryStart -= self.__onServerUpdate
        g_preDefinedHosts.onPingPerformed -= self.__onServerUpdate
        g_preDefinedHosts.onCsisQueryComplete -= self.__onServerUpdate
        self._serverList = None
        return

    def updateServerList(self):
        self._setServerList(g_preDefinedHosts.shortList())

    def _setServerList(self, baseServerList):
        self._serverList = []
        self._selectedServerIdx = 0
        serverName = self._loginPreferences['server_name']
        for idx, (hostName, friendlyName, csisStatus, _) in enumerate(baseServerList):
            if serverName == hostName:
                self._selectedServerIdx = idx
            self._serverList.append({'label': friendlyName, 
               'data': hostName, 
               'csisStatus': csisStatus})

    def startListenCsisQuery(self, startListen):
        if GUI_SETTINGS.csisRequestRate == REQUEST_RATE.ON_REQUEST:
            if startListen:
                g_preDefinedHosts.startCSISUpdate()
            else:
                g_preDefinedHosts.stopCSISUpdate()
        if startListen:
            g_preDefinedHosts.requestPing(True)

    def setServerPreselection(self, peripheryId):
        hostItem = g_preDefinedHosts.periphery(peripheryId)
        if hostItem is not None:
            self._loginPreferences['server_name'] = hostItem.url
            self.updateServerList()
        return

    @property
    def serverList(self):
        return self._serverList

    @property
    def selectedServerIdx(self):
        return self._selectedServerIdx

    @property
    def selectedServer(self):
        if self._selectedServerIdx < len(self._serverList):
            return self._serverList[self._selectedServerIdx]
        else:
            return

    def __onServerUpdate(self, _=None):
        self.updateServerList()
        self.onServersStatusChanged(self._serverList)


class DevelopmentServers(Servers):

    def __init__(self, loginPreferences):
        Servers.__init__(self, loginPreferences)
        BigWorld.serverDiscovery.changeNotifier = self.updateServerList

    def fini(self):
        Servers.fini(self)
        BigWorld.serverDiscovery.searching = 0

    def updateServerList(self):

        def _serverDottedHost(ip):
            return '%d.%d.%d.%d' % (
             ip >> 24 & 255,
             ip >> 16 & 255,
             ip >> 8 & 255,
             ip >> 0 & 255)

        def _serverNetName(details):
            name = _serverDottedHost(details.ip)
            if details.port:
                name += ':%d' % details.port
                return name

        def _serverNiceName(details):
            name = details.hostName
            if not name:
                name = _serverNetName(details)
            elif details.port:
                name += ':%d' % details.port
            if details.ownerName:
                name += ' (' + details.ownerName + ')'
            return name

        servers = [ (_serverNiceName(server), server.serverString) for server in BigWorld.serverDiscovery.servers
                  ]
        baseServerList = g_preDefinedHosts.shortList()
        for friendlyName, hostName in servers:
            if not g_preDefinedHosts.predefined(hostName):
                baseServerList.append((
                 hostName,
                 friendlyName,
                 g_preDefinedHosts.getDefaultCSISStatus(),
                 None))

        self._setServerList(baseServerList)
        return