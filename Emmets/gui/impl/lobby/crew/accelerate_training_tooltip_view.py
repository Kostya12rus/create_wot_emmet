# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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