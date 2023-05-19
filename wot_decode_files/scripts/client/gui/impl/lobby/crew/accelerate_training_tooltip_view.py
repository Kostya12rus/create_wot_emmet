# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/accelerate_training_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.accelerate_training_tooltip_view_model import AccelerateTrainingTooltipViewModel
from gui.impl.pub import ViewImpl

class AccelerateTrainingTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(layoutID=R.views.lobby.crew.AccelerateTrainingTooltipView(), model=AccelerateTrainingTooltipViewModel())
        super(AccelerateTrainingTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(AccelerateTrainingTooltipView, self).getViewModel()