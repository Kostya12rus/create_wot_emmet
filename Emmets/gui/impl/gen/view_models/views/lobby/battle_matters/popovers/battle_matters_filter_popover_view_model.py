# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/popovers/battle_matters_filter_popover_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.popovers.filter_control_view_model import FilterControlViewModel

class BattleMattersFilterPopoverViewModel(ViewModel):
    __slots__ = ('onToggleFilter', )
    ARG_CONTROL_TYPE = 'name'
    ARG_CONTROL_NATION = 'nation'

    def __init__(self, properties=2, commands=1):
        super(BattleMattersFilterPopoverViewModel, self).__init__(properties=properties, commands=commands)

    def getTypes(self):
        return self._getArray(0)

    def setTypes(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTypesType():
        return FilterControlViewModel

    def getNations(self):
        return self._getArray(1)

    def setNations(self, value):
        self._setArray(1, value)

    @staticmethod
    def getNationsType():
        return FilterControlViewModel

    def _initialize(self):
        super(BattleMattersFilterPopoverViewModel, self)._initialize()
        self._addArrayProperty('types', Array())
        self._addArrayProperty('nations', Array())
        self.onToggleFilter = self._addCommand('onToggleFilter')