# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/web.py


class IWebController(object):

    def addListener(self, listener):
        raise NotImplementedError

    def removeListener(self, listener):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def invalidate(self):
        raise NotImplementedError

    def getClanDossier(self, clanDbID=None):
        raise NotImplementedError

    def login(self, callback):
        raise NotImplementedError

    def resyncLogin(self, forceLogin=False):
        raise NotImplementedError

    def sendRequest(self, ctx, callback=None, allowDelay=None):
        raise NotImplementedError

    def getStateID(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    def getWebRequester(self):
        raise NotImplementedError

    def getAccountProfile(self):
        raise NotImplementedError

    def getLimits(self):
        raise NotImplementedError

    def getClanDbID(self):
        raise NotImplementedError

    def changeState(self, state):
        raise NotImplementedError

    def onStateUpdated(self):
        raise NotImplementedError

    def isLoggedOn(self):
        raise NotImplementedError

    def updateClanCommonDataCache(self, cache):
        raise NotImplementedError

    def clearClanCommonDataCache(self):
        raise NotImplementedError

    def getClanCommonData(self, clanDbID):
        raise NotImplementedError

    def requestUsers(self, dbIDs, callback):
        raise NotImplementedError

    def getAccessTokenData(self, force, callback=None):
        raise NotImplementedError