# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/tooltips/ny_menu_gift_tooltip_model.py
from frameworks.wulf import ViewModel

class NyMenuGiftTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyMenuGiftTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsBalanceAllowed(self):
        return self._getBool(0)

    def setIsBalanceAllowed(self, value):
        self._setBool(0, value)

    def getPostStampsCount(self):
        return self._getNumber(1)

    def setPostStampsCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(NyMenuGiftTooltipModel, self)._initialize()
        self._addBoolProperty('isBalanceAllowed', False)
        self._addNumberProperty('postStampsCount', 0)