# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/subscription/wot_plus_tooltip.py
from typing import TYPE_CHECKING
from frameworks.wulf import ViewSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.subscription.wot_plus_tooltip_model import WotPlusTooltipModel
from gui.impl.pub import ViewImpl
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from uilogging.wot_plus.loggers import WotPlusHeaderTooltipLogger
if TYPE_CHECKING:
    from typing import List
    from gui.server_events.bonuses import WoTPlusBonus
    from gui.shared.missions.packers.bonus import BaseBonusUIPacker

class WotPlusTooltip(ViewImpl):
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.subscription.WotPlusTooltip())
        settings.model = WotPlusTooltipModel()
        self._uiLogger = WotPlusHeaderTooltipLogger()
        super(WotPlusTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(WotPlusTooltip, self).getViewModel()

    def _onLoading(self):
        super(WotPlusTooltip, self)._onLoading()
        with self.viewModel.transaction() as (model):
            model.setExpirationDate(backport.getShortDateFormat(self._wotPlusCtrl.getExpiryTime()))
            if self._wotPlusCtrl.getNextBillingTime():
                model.setNextCharge(backport.getShortDateFormat(self._wotPlusCtrl.getNextBillingTime()))
            model.setState(self._wotPlusCtrl.getState())
            bonuses = self._wotPlusCtrl.getEnabledBonuses()
            bonusList = model.getBonuses()
            bonusList.clear()
            bonusList.reserve(len(bonuses))
            packerMap = getDefaultBonusPackersMap()
            for bonus in bonuses:
                packer = packerMap.get(bonus.getName())
                if packer:
                    for bonusModel in packer.pack(bonus):
                        bonusList.addViewModel(bonusModel)

            bonusList.invalidate()

    def _initialize(self, *args, **kwargs):
        super(WotPlusTooltip, self)._initialize(*args, **kwargs)
        self._uiLogger.onViewInitialize()

    def _finalize(self):
        super(WotPlusTooltip, self)._finalize()
        self._uiLogger.onViewFinalize(self._wotPlusCtrl.getState())