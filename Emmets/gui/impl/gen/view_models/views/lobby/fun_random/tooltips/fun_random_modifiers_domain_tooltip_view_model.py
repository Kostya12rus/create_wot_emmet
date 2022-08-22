# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/fun_random/tooltips/fun_random_modifiers_domain_tooltip_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_modifiers.modifier_model import ModifierModel

class FunRandomModifiersDomainTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FunRandomModifiersDomainTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getModifiersDomain(self):
        return self._getString(0)

    def setModifiersDomain(self, value):
        self._setString(0, value)

    def getModifiers(self):
        return self._getArray(1)

    def setModifiers(self, value):
        self._setArray(1, value)

    @staticmethod
    def getModifiersType():
        return ModifierModel

    def _initialize(self):
        super(FunRandomModifiersDomainTooltipViewModel, self)._initialize()
        self._addStringProperty('modifiersDomain', '')
        self._addArrayProperty('modifiers', Array())