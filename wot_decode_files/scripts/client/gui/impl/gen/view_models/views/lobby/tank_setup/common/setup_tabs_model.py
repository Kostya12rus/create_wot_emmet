# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/setup_tabs_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.setup_tab_model import SetupTabModel

class SetupTabsModel(ViewModel):
    __slots__ = ('onTabChanged', )

    def __init__(self, properties=2, commands=1):
        super(SetupTabsModel, self).__init__(properties=properties, commands=commands)

    def getTabs(self):
        return self._getArray(0)

    def setTabs(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTabsType():
        return SetupTabModel

    def getSelectedTabName(self):
        return self._getString(1)

    def setSelectedTabName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(SetupTabsModel, self)._initialize()
        self._addArrayProperty('tabs', Array())
        self._addStringProperty('selectedTabName', '')
        self.onTabChanged = self._addCommand('onTabChanged')