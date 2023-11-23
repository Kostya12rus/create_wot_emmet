# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/quick_training_discount_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.quick_training_discount_tooltip_model import QuickTrainingDiscountTooltipModel
from gui.impl.pub import ViewImpl

class QuickTrainingDiscountTooltip(ViewImpl):
    __slots__ = ('_oldFreeXpBase', '_newFreeXpBase', '_oldXpExchange', '_newXpExchange')

    def __init__(self, oldFreeXpBase, newFreeXpBase, oldXpExchange, newXpExchange):
        self._oldFreeXpBase = oldFreeXpBase
        self._newFreeXpBase = newFreeXpBase
        self._oldXpExchange = oldXpExchange
        self._newXpExchange = newXpExchange
        settings = ViewSettings(R.views.lobby.crew.tooltips.QuickTrainingDiscountTooltip(), model=QuickTrainingDiscountTooltipModel())
        super(QuickTrainingDiscountTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(QuickTrainingDiscountTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (vm):
            vm.setOldFreeXpBaseValue(self._oldFreeXpBase)
            vm.setNewFreeXpBaseValue(self._newFreeXpBase)
            vm.setOldXpExchangeValue(self._oldXpExchange)
            vm.setNewXpExchangeValue(self._newXpExchange)