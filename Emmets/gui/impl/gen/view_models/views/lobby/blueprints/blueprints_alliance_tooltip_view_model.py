# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprints_alliance_tooltip_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_price import BlueprintPrice

class BlueprintsAllianceTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BlueprintsAllianceTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getPriceOptions(self):
        return self._getArray(0)

    def setPriceOptions(self, value):
        self._setArray(0, value)

    @staticmethod
    def getPriceOptionsType():
        return BlueprintPrice

    def getVehicleNationName(self):
        return self._getString(1)

    def setVehicleNationName(self, value):
        self._setString(1, value)

    def getAllianceName(self):
        return self._getString(2)

    def setAllianceName(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(BlueprintsAllianceTooltipViewModel, self)._initialize()
        self._addArrayProperty('priceOptions', Array())
        self._addStringProperty('vehicleNationName', '')
        self._addStringProperty('allianceName', '')