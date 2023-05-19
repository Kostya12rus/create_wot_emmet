# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_post_progression/tooltips/base_feature_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.feature_tooltip_view_model import FeatureTooltipViewModel
from gui.impl.pub import ViewImpl

class BaseFeatureTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID, model, *args, **kwargs):
        settings = ViewSettings(layoutID)
        settings.model = model
        settings.args = args
        settings.kwargs = kwargs
        super(BaseFeatureTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BaseFeatureTooltipView, self).getViewModel()

    def _onLoading(self, step, *args, **kwargs):
        super(BaseFeatureTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setLevel(step.getLevel())
            model.setIsUnlocked(step.isReceived())
            model.setIsDisabled(step.action.isDisabled())