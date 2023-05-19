# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/messenger.py


class IMessengerEntry(object):

    @property
    def protos(self):
        raise NotImplementedError

    @property
    def storage(self):
        raise NotImplementedError

    @property
    def gui(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def onAccountShowGUI(self):
        raise NotImplementedError

    def onAvatarInitGUI(self):
        raise NotImplementedError

    def onAvatarShowGUI(self):
        raise NotImplementedError