# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/reroll_tooltip.py
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen.view_models.views.reroll_tooltip_model import RerollTooltipModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class RerollTooltip(ViewImpl):

    def __init__(self, timeLeft, rerollInterval, withCountdown=False):
        self._timeLeft = timeLeft
        self._rerollInterval = rerollInterval
        settings = ViewSettings(R.views.lobby.missions.RerollTooltipWithCountdown() if withCountdown else R.views.lobby.missions.RerollTooltip(), model=RerollTooltipModel())
        super(RerollTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RerollTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        self.viewModel.setTimeLeft(self._timeLeft)
        self.viewModel.setRerollInterval(self._rerollInterval)