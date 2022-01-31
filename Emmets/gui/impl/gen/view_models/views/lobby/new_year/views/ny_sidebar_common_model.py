# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/views/ny_sidebar_common_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.components.new_year_tab_model import NewYearTabModel

class NySidebarCommonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NySidebarCommonModel, self).__init__(properties=properties, commands=commands)

    def getItemsTabBar(self):
        return self._getArray(0)

    def setItemsTabBar(self, value):
        self._setArray(0, value)

    def getStartIndex(self):
        return self._getNumber(1)

    def setStartIndex(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(NySidebarCommonModel, self)._initialize()
        self._addArrayProperty('itemsTabBar', Array())
        self._addNumberProperty('startIndex', 0)