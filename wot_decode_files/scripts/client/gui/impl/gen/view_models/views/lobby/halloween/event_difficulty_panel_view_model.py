# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/event_difficulty_panel_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.halloween.event_difficulty_item_model import EventDifficultyItemModel

class EventDifficultyPanelViewModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=2, commands=1):
        super(EventDifficultyPanelViewModel, self).__init__(properties=properties, commands=commands)

    def getIsDifficultyWindow(self):
        return self._getBool(0)

    def setIsDifficultyWindow(self, value):
        self._setBool(0, value)

    def getDifficulties(self):
        return self._getArray(1)

    def setDifficulties(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(EventDifficultyPanelViewModel, self)._initialize()
        self._addBoolProperty('isDifficultyWindow', False)
        self._addArrayProperty('difficulties', Array())
        self.onClick = self._addCommand('onClick')