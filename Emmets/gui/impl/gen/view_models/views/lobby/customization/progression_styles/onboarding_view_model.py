# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/progression_styles/onboarding_view_model.py
from frameworks.wulf import ViewModel

class OnboardingViewModel(ViewModel):
    __slots__ = ('onClose', 'onGotoStyle')

    def __init__(self, properties=1, commands=2):
        super(OnboardingViewModel, self).__init__(properties=properties, commands=commands)

    def getIsFirstShow(self):
        return self._getBool(0)

    def setIsFirstShow(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(OnboardingViewModel, self)._initialize()
        self._addBoolProperty('isFirstShow', False)
        self.onClose = self._addCommand('onClose')
        self.onGotoStyle = self._addCommand('onGotoStyle')