# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/trophy_device_confirm_dialog_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class TrophyDeviceConfirmDialogModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TrophyDeviceConfirmDialogModel, self).__init__(properties=properties, commands=commands)

    def getTrophyBasicName(self):
        return self._getString(0)

    def setTrophyBasicName(self, value):
        self._setString(0, value)

    def getTrophyBasicImg(self):
        return self._getString(1)

    def setTrophyBasicImg(self, value):
        self._setString(1, value)

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)

    def getCredits(self):
        return self._getString(3)

    def setCredits(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(TrophyDeviceConfirmDialogModel, self)._initialize()
        self._addStringProperty('trophyBasicName', '')
        self._addStringProperty('trophyBasicImg', '')
        self._addArrayProperty('bonuses', Array())
        self._addStringProperty('credits', '')