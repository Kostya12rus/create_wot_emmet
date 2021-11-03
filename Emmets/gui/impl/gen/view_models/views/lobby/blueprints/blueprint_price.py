# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_price.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_value_price import BlueprintValuePrice

class BlueprintPrice(BlueprintValuePrice):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(BlueprintPrice, self).__init__(properties=properties, commands=commands)

    def getIconBig(self):
        return self._getResource(7)

    def setIconBig(self, value):
        self._setResource(7, value)

    def getNationName(self):
        return self._getString(8)

    def setNationName(self, value):
        self._setString(8, value)

    def getValue(self):
        return self._getNumber(9)

    def setValue(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(BlueprintPrice, self)._initialize()
        self._addResourceProperty('iconBig', R.invalid())
        self._addStringProperty('nationName', '')
        self._addNumberProperty('value', 0)