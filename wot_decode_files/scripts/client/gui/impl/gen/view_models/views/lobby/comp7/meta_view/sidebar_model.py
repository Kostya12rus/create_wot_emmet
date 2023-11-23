# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/sidebar_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.tab_model import TabModel

class SidebarModel(ViewModel):
    __slots__ = ('onSideBarTabChange', )

    def __init__(self, properties=1, commands=1):
        super(SidebarModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getItemsType():
        return TabModel

    def _initialize(self):
        super(SidebarModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self.onSideBarTabChange = self._addCommand('onSideBarTabChange')