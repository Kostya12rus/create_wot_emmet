# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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