# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/compare_modifications_panel_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_step_model import CompareStepModel

class CompareModificationsPanelViewModel(ViewModel):
    __slots__ = ('onClearModifications', 'onConfigureModifications', 'onClose')

    def __init__(self, properties=2, commands=3):
        super(CompareModificationsPanelViewModel, self).__init__(properties=properties, commands=commands)

    def getIsEmpty(self):
        return self._getBool(0)

    def setIsEmpty(self, value):
        self._setBool(0, value)

    def getSteps(self):
        return self._getArray(1)

    def setSteps(self, value):
        self._setArray(1, value)

    @staticmethod
    def getStepsType():
        return CompareStepModel

    def _initialize(self):
        super(CompareModificationsPanelViewModel, self)._initialize()
        self._addBoolProperty('isEmpty', True)
        self._addArrayProperty('steps', Array())
        self.onClearModifications = self._addCommand('onClearModifications')
        self.onConfigureModifications = self._addCommand('onConfigureModifications')
        self.onClose = self._addCommand('onClose')