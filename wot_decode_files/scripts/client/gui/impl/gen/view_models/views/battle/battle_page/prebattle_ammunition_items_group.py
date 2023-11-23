# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_items_group.py
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_setup_selector import PrebattleAmmunitionSetupSelector
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_group import AmmunitionItemsGroup

class PrebattleAmmunitionItemsGroup(AmmunitionItemsGroup):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(PrebattleAmmunitionItemsGroup, self).__init__(properties=properties, commands=commands)

    @property
    def setupSelector(self):
        return self._getViewModel(5)

    @staticmethod
    def getSetupSelectorType():
        return PrebattleAmmunitionSetupSelector

    def _initialize(self):
        super(PrebattleAmmunitionItemsGroup, self)._initialize()
        self._addViewModelProperty('setupSelector', PrebattleAmmunitionSetupSelector())