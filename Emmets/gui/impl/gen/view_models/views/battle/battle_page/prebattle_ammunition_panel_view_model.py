# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_panel_view_model.py
from enum import IntEnum
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_panel_model import PrebattleAmmunitionPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class State(IntEnum):
    BATTLELOADING = 0
    PREBATTLE = 1
    PREBATTLENOTCONFIRMED = 2


class PrebattleAmmunitionPanelViewModel(AmmunitionPanelViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=2):
        super(PrebattleAmmunitionPanelViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def ammunitionPanel(self):
        return self._getViewModel(7)

    @staticmethod
    def getAmmunitionPanelType():
        return PrebattleAmmunitionPanelModel

    def getTimeTillBattleStart(self):
        return self._getNumber(8)

    def setTimeTillBattleStart(self, value):
        self._setNumber(8, value)

    def getState(self):
        return State(self._getNumber(9))

    def setState(self, value):
        self._setNumber(9, value.value)

    def _initialize(self):
        super(PrebattleAmmunitionPanelViewModel, self)._initialize()
        self._addViewModelProperty('ammunitionPanel', PrebattleAmmunitionPanelModel())
        self._addNumberProperty('timeTillBattleStart', 0)
        self._addNumberProperty('state')