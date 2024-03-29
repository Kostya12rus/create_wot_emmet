# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/daily_experience_view_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.daily_experience_base_model import DailyExperienceBaseModel

class DailyExperienceViewModel(DailyExperienceBaseModel):
    __slots__ = ('onGoToContentPage', 'onBackBtnClicked')

    def __init__(self, properties=5, commands=2):
        super(DailyExperienceViewModel, self).__init__(properties=properties, commands=commands)

    def getBackBtnLabel(self):
        return self._getResource(4)

    def setBackBtnLabel(self, value):
        self._setResource(4, value)

    def _initialize(self):
        super(DailyExperienceViewModel, self)._initialize()
        self._addResourceProperty('backBtnLabel', R.invalid())
        self.onGoToContentPage = self._addCommand('onGoToContentPage')
        self.onBackBtnClicked = self._addCommand('onBackBtnClicked')