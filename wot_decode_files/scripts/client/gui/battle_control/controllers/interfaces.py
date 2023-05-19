# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/interfaces.py


class IBattleController(object):
    __slots__ = ()

    def startControl(self, *args):
        raise NotImplementedError

    def stopControl(self):
        raise NotImplementedError

    def getControllerID(self):
        raise NotImplementedError


class IBattleControllersRepository(object):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def getController(self, ctrlID):
        raise NotImplementedError

    def addController(self, ctrl):
        raise NotImplementedError