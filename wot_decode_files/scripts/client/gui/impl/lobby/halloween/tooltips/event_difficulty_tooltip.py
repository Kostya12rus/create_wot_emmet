# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/halloween/tooltips/event_difficulty_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.halloween.tooltips.event_difficulty_tooltip_model import EventDifficultyTooltipModel, StateEnum
from gui.impl.pub import ViewImpl

class EventDifficultyTooltip(ViewImpl):

    def __init__(self, level, isSelected, isLocked, currentProgress, totalProgress):
        settings = ViewSettings(R.views.lobby.halloween.tooltips.EventDifficultyTooltip())
        settings.model = EventDifficultyTooltipModel()
        self.__level = level
        self.__isSelected = isSelected
        self.__isLocked = isLocked
        self.__currentProgress = currentProgress
        self.__totalProgress = totalProgress
        super(EventDifficultyTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(EventDifficultyTooltip, self).getViewModel()

    def _onLoading(self):
        super(EventDifficultyTooltip, self)._onLoading()
        self.__fillModel()

    def __fillModel(self):
        with self.viewModel.transaction() as (vm):
            vm.setLevel(self.__level)
            vm.setCurrent(self.__currentProgress)
            vm.setTotal(self.__totalProgress)
            if self.__isSelected:
                vm.setState(StateEnum.SELECTED)
            elif self.__isLocked:
                vm.setState(StateEnum.LOCKED)
            else:
                vm.setState(StateEnum.DEFAULT)