# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/ammunition_buy_model.py
from gui.impl.gen.view_models.views.lobby.common.dialog_with_exchange import DialogWithExchange
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.ammunition_buy_content import AmmunitionBuyContent

class AmmunitionBuyModel(DialogWithExchange):
    __slots__ = ()

    def __init__(self, properties=18, commands=3):
        super(AmmunitionBuyModel, self).__init__(properties=properties, commands=commands)

    @property
    def mainContent(self):
        return self._getViewModel(15)

    @property
    def dealPanel(self):
        return self._getViewModel(16)

    def getWithRollback(self):
        return self._getBool(17)

    def setWithRollback(self, value):
        self._setBool(17, value)

    def _initialize(self):
        super(AmmunitionBuyModel, self)._initialize()
        self._addViewModelProperty('mainContent', AmmunitionBuyContent())
        self._addViewModelProperty('dealPanel', DealPanelModel())
        self._addBoolProperty('withRollback', False)