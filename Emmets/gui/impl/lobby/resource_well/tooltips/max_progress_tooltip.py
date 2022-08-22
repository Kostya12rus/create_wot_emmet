# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/resource_well/tooltips/max_progress_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.resource_well.tooltips.max_progress_tooltip_model import MaxProgressTooltipModel
from gui.impl.pub import ViewImpl

class MaxProgressTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.resource_well.tooltips.MaxProgressTooltip())
        settings.model = MaxProgressTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(MaxProgressTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MaxProgressTooltip, self).getViewModel()

    def _onLoading(self, currentValue, maxValue, resourceType, *args, **kwargs):
        super(MaxProgressTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setCurrentValue(currentValue)
            model.setMaxValue(maxValue)
            model.setResourceType(resourceType)