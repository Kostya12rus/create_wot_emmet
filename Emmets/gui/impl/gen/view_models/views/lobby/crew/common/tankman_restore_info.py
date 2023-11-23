# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/tankman_restore_info.py
from frameworks.wulf import ViewModel

class TankmanRestoreInfo(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TankmanRestoreInfo, self).__init__(properties=properties, commands=commands)

    def getFreePeriod(self):
        return self._getNumber(0)

    def setFreePeriod(self, value):
        self._setNumber(0, value)

    def getPaidPeriod(self):
        return self._getNumber(1)

    def setPaidPeriod(self, value):
        self._setNumber(1, value)

    def getRecoverPrice(self):
        return self._getNumber(2)

    def setRecoverPrice(self, value):
        self._setNumber(2, value)

    def getMembersBuffer(self):
        return self._getNumber(3)

    def setMembersBuffer(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(TankmanRestoreInfo, self)._initialize()
        self._addNumberProperty('freePeriod', 0)
        self._addNumberProperty('paidPeriod', 0)
        self._addNumberProperty('recoverPrice', 0)
        self._addNumberProperty('membersBuffer', 0)