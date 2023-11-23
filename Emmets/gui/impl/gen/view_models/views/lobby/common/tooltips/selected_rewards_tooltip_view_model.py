# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/tooltips/selected_rewards_tooltip_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_category_model import SelectedRewardsTooltipCategoryModel

class SelectedRewardsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SelectedRewardsTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getCategories(self):
        return self._getArray(0)

    def setCategories(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCategoriesType():
        return SelectedRewardsTooltipCategoryModel

    def getTotalSelected(self):
        return self._getNumber(1)

    def setTotalSelected(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(SelectedRewardsTooltipViewModel, self)._initialize()
        self._addArrayProperty('categories', Array())
        self._addNumberProperty('totalSelected', 0)