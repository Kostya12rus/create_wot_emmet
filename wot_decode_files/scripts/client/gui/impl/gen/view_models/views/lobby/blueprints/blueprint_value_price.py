# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_value_price.py
from gui.impl.gen.view_models.views.value_price import ValuePrice

class BlueprintValuePrice(ValuePrice):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BlueprintValuePrice, self).__init__(properties=properties, commands=commands)

    def getHasDelimeter(self):
        return self._getBool(4)

    def setHasDelimeter(self, value):
        self._setBool(4, value)

    def getItemCD(self):
        return self._getNumber(5)

    def setItemCD(self, value):
        self._setNumber(5, value)

    def getTooltipId(self):
        return self._getString(6)

    def setTooltipId(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(BlueprintValuePrice, self)._initialize()
        self._addBoolProperty('hasDelimeter', False)
        self._addNumberProperty('itemCD', 0)
        self._addStringProperty('tooltipId', '')