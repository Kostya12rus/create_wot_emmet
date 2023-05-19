# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_grid_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel

class PostProgressionGridModel(ViewModel):
    __slots__ = ('onMainStepActionClick', 'onMainStepSelectClick', 'onMultiStepActionClick',
                 'onMultiStepSelectClick', 'onPrebattleSwitchToggleClick')

    def __init__(self, properties=3, commands=5):
        super(PostProgressionGridModel, self).__init__(properties=properties, commands=commands)

    def getMainSelectedIdx(self):
        return self._getNumber(0)

    def setMainSelectedIdx(self, value):
        self._setNumber(0, value)

    def getMainSteps(self):
        return self._getArray(1)

    def setMainSteps(self, value):
        self._setArray(1, value)

    @staticmethod
    def getMainStepsType():
        return SingleStepModel

    def getMultiSteps(self):
        return self._getArray(2)

    def setMultiSteps(self, value):
        self._setArray(2, value)

    @staticmethod
    def getMultiStepsType():
        return MultiStepModel

    def _initialize(self):
        super(PostProgressionGridModel, self)._initialize()
        self._addNumberProperty('mainSelectedIdx', -1)
        self._addArrayProperty('mainSteps', Array())
        self._addArrayProperty('multiSteps', Array())
        self.onMainStepActionClick = self._addCommand('onMainStepActionClick')
        self.onMainStepSelectClick = self._addCommand('onMainStepSelectClick')
        self.onMultiStepActionClick = self._addCommand('onMultiStepActionClick')
        self.onMultiStepSelectClick = self._addCommand('onMultiStepSelectClick')
        self.onPrebattleSwitchToggleClick = self._addCommand('onPrebattleSwitchToggleClick')