# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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