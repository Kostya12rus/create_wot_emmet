# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lunar_ny/friend_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class FriendStatus(IntEnum):
    ONLINE = 0
    OFFLINE = 1


class FriendModel(ViewModel):
    __slots__ = ()
    NOT_SELECTED_SPA_ID = 0

    def __init__(self, properties=4, commands=0):
        super(FriendModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getClan(self):
        return self._getString(1)

    def setClan(self, value):
        self._setString(1, value)

    def getSpaID(self):
        return self._getNumber(2)

    def setSpaID(self, value):
        self._setNumber(2, value)

    def getStatus(self):
        return FriendStatus(self._getNumber(3))

    def setStatus(self, value):
        self._setNumber(3, value.value)

    def _initialize(self):
        super(FriendModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('clan', '')
        self._addNumberProperty('spaID', 0)
        self._addNumberProperty('status')