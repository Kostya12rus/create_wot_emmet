# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/difficulty_window_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class WindowTypeEnum(Enum):
    MEDIUM = 'medium'
    HARD = 'hard'


class DifficultyWindowViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=1, commands=1):
        super(DifficultyWindowViewModel, self).__init__(properties=properties, commands=commands)

    def getWindowType(self):
        return WindowTypeEnum(self._getString(0))

    def setWindowType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(DifficultyWindowViewModel, self)._initialize()
        self._addStringProperty('windowType')
        self.onClose = self._addCommand('onClose')