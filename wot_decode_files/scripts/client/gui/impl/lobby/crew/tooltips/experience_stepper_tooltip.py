# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/experience_stepper_tooltip.py
from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class ExperienceStepperTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.lobby.crew.tooltips.ExperienceStepperTooltip(), model=ViewModel())
        super(ExperienceStepperTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ExperienceStepperTooltip, self).getViewModel()