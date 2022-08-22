# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/wot_anniversary/wot_anniversary_entry_point_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class State(IntEnum):
    NEWQUESTS = 0
    INPROGRESS = 1
    DONE = 2
    NOQUESTS = 3


class WotAnniversaryEntryPointModel(ViewModel):
    __slots__ = ('onWidgetClick', )

    def __init__(self, properties=2, commands=1):
        super(WotAnniversaryEntryPointModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return State(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)

    def getBalance(self):
        return self._getNumber(1)

    def setBalance(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(WotAnniversaryEntryPointModel, self)._initialize()
        self._addNumberProperty('state')
        self._addNumberProperty('balance', -1)
        self.onWidgetClick = self._addCommand('onWidgetClick')