# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/platoon/tooltip/platoon_event_tooltip.py
from gui.impl.gen import R
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.lobby.platoon.event_difficulty_model import EventDifficultyModel

class EventTooltip(ViewImpl):

    def __init__(self, level, header='', body=''):
        self.__header = header
        self.__body = body
        self.__level = level
        settings = ViewSettings(R.views.lobby.platoon.EventTooltips(), model=EventDifficultyModel())
        super(EventTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (model):
            model.setTooltipDifficultyHeader(self.__header)
            model.setTooltipDifficulty(self.__body)
            model.setLevel(self.__level)