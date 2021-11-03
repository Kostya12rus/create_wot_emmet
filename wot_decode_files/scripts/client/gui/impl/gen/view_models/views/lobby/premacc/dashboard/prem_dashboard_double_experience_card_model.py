# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/prem_dashboard_double_experience_card_model.py
from gui.impl.gen.view_models.views.lobby.premacc.daily_experience_base_model import DailyExperienceBaseModel

class PremDashboardDoubleExperienceCardModel(DailyExperienceBaseModel):
    __slots__ = ('onGoToDoubleExpView', )

    def __init__(self, properties=5, commands=1):
        super(PremDashboardDoubleExperienceCardModel, self).__init__(properties=properties, commands=commands)

    def getIsAvailable(self):
        return self._getBool(4)

    def setIsAvailable(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(PremDashboardDoubleExperienceCardModel, self)._initialize()
        self._addBoolProperty('isAvailable', True)
        self.onGoToDoubleExpView = self._addCommand('onGoToDoubleExpView')