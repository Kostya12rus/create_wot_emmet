# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/subscription/wot_plus_tooltip_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class SubscriptionState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1
    CANCELED = 2


class WotPlusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(WotPlusTooltipModel, self).__init__(properties=properties, commands=commands)

    def getNextCharge(self):
        return self._getString(0)

    def setNextCharge(self, value):
        self._setString(0, value)

    def getState(self):
        return SubscriptionState(self._getNumber(1))

    def setState(self, value):
        self._setNumber(1, value.value)

    def _initialize(self):
        super(WotPlusTooltipModel, self)._initialize()
        self._addStringProperty('nextCharge', '')
        self._addNumberProperty('state')