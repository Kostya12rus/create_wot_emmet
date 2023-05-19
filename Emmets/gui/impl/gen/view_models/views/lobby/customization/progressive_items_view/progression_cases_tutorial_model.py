# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/progressive_items_view/progression_cases_tutorial_model.py
from frameworks.wulf import ViewModel

class ProgressionCasesTutorialModel(ViewModel):
    __slots__ = ('onClose', 'showVideo')

    def __init__(self, properties=0, commands=2):
        super(ProgressionCasesTutorialModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ProgressionCasesTutorialModel, self)._initialize()
        self.onClose = self._addCommand('onClose')
        self.showVideo = self._addCommand('showVideo')