# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/missions/missions_tab_bar_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class MissionsTabBarViewModel(ViewModel):
    __slots__ = ('onTabSelectionChanged', )

    def __init__(self, properties=3, commands=1):
        super(MissionsTabBarViewModel, self).__init__(properties=properties, commands=commands)

    def getViews(self):
        return self._getArray(0)

    def setViews(self, value):
        self._setArray(0, value)

    def getCurrentView(self):
        return self._getString(1)

    def setCurrentView(self, value):
        self._setString(1, value)

    def getStartIndex(self):
        return self._getNumber(2)

    def setStartIndex(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(MissionsTabBarViewModel, self)._initialize()
        self._addArrayProperty('views', Array())
        self._addStringProperty('currentView', '')
        self._addNumberProperty('startIndex', 0)
        self.onTabSelectionChanged = self._addCommand('onTabSelectionChanged')