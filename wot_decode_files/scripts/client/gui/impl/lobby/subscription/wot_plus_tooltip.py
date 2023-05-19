# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/subscription/wot_plus_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.subscription.wot_plus_tooltip_model import WotPlusTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from uilogging.wot_plus.loggers import WotPlusHeaderTooltipLogger

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
            model.setNextCharge(backport.getShortDateFormat(self._wotPlusCtrl.getExpiryTime()))
            model.setState(self._wotPlusCtrl.getState())

    def _initialize(self, *args, **kwargs):
        super(WotPlusTooltip, self)._initialize(*args, **kwargs)
        self._uiLogger.onViewInitialize()

    def _finalize(self):
        super(WotPlusTooltip, self)._finalize()
        self._uiLogger.onViewFinalize(self._wotPlusCtrl.getState())