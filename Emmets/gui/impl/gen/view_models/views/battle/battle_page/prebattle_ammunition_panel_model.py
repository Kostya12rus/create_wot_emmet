# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_panel_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_items_group import PrebattleAmmunitionItemsGroup
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_model import AmmunitionPanelModel

class PrebattleAmmunitionPanelModel(AmmunitionPanelModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=6):
        super(PrebattleAmmunitionPanelModel, self).__init__(properties=properties, commands=commands)

    def getSectionGroups(self):
        return self._getArray(6)

    def setSectionGroups(self, value):
        self._setArray(6, value)

    @staticmethod
    def getSectionGroupsType():
        return PrebattleAmmunitionItemsGroup

    def _initialize(self):
        super(PrebattleAmmunitionPanelModel, self)._initialize()
        self._addArrayProperty('sectionGroups', Array())