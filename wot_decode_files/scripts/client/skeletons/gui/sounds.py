# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/sounds.py


class ISoundsController(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self, isDisconnected=False):
        raise NotImplementedError

    @property
    def system(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def setEnvForSpace(self, spaceID, newEnv):
        raise NotImplementedError