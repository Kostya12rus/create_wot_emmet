# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/view_interface.py


class ViewInterface(object):

    @property
    def uiImpl(self):
        raise NotImplementedError

    @property
    def layer(self):
        raise NotImplementedError

    @property
    def viewScope(self):
        raise NotImplementedError

    @property
    def key(self):
        raise NotImplementedError

    @property
    def alias(self):
        raise NotImplementedError

    @property
    def uniqueName(self):
        raise NotImplementedError

    @property
    def settings(self):
        raise NotImplementedError

    @property
    def soundManager(self):
        raise NotImplementedError

    def isViewModal(self):
        raise NotImplementedError

    def getAlias(self):
        raise NotImplementedError

    def setAlias(self, alias):
        raise NotImplementedError

    def getSubContainersSettings(self):
        raise NotImplementedError

    def getUniqueName(self):
        raise NotImplementedError

    def setUniqueName(self, name):
        raise NotImplementedError

    def getCurrentScope(self):
        raise NotImplementedError

    def setCurrentScope(self, scope):
        raise NotImplementedError