# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_post_progression/tooltips/setup_tooltip_view.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.setup_tooltip_view_model import SetupTooltipViewModel, SetupFeatureType
from gui.impl.lobby.veh_post_progression.tooltips.base_feature_tooltip_view import BaseFeatureTooltipView

class SetupTooltipView(BaseFeatureTooltipView):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(SetupTooltipView, self).__init__(R.views.lobby.veh_post_progression.tooltip.SetupTooltipView(), SetupTooltipViewModel(), *args, **kwargs)

    @property
    def viewModel(self):
        return super(SetupTooltipView, self).getViewModel()

    def _onLoading(self, step, *args, **kwargs):
        super(SetupTooltipView, self)._onLoading(step, *args, **kwargs)
        feature = step.action
        with self.viewModel.transaction() as (model):
            model.setIconName(feature.getImageName())
            model.setType(SetupFeatureType(feature.getTechName()))