# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/prb_control.py


class IPrbControlLoader(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def getDispatcher(self):
        raise NotImplementedError

    def getInvitesManager(self):
        raise NotImplementedError

    def getAutoInvitesNotifier(self):
        raise NotImplementedError

    def getPeripheriesHandler(self):
        raise NotImplementedError

    def getStorage(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def setEnabled(self, enabled):
        raise NotImplementedError

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError

    def onAvatarBecomePlayer(self):
        raise NotImplementedError

    def onDisconnected(self):
        raise NotImplementedError