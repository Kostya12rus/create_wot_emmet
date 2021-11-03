# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/commander_cmp_perk_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class CommanderCmpPerkModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CommanderCmpPerkModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)

    def getTooltipID(self):
        return self._getString(1)

    def setTooltipID(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(CommanderCmpPerkModel, self)._initialize()
        self._addResourceProperty('icon', R.invalid())
        self._addStringProperty('tooltipID', '')