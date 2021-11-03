# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/afk_controller.py


class IAFKController(object):
    onBanUpdated = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    @property
    def isBanned(self):
        return False

    @property
    def banExpiryTime(self):
        return 0

    def showBanWindow(self):
        raise NotImplementedError

    def showWarningWindow(self):
        raise NotImplementedError

    def showQuest(self):
        raise NotImplementedError

    def questFilter(self, quest):
        raise NotImplementedError

    def showAFKWindows(self):
        raise NotImplementedError