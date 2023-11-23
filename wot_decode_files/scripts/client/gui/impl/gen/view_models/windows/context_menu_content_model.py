# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/context_menu_content_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class ContextMenuContentModel(ViewModel):
    __slots__ = ('onItemClicked', )

    def __init__(self, properties=3, commands=1):
        super(ContextMenuContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def contextMenuList(self):
        return self._getViewModel(0)

    @staticmethod
    def getContextMenuListType():
        return ListModel

    def getItemsCount(self):
        return self._getNumber(1)

    def setItemsCount(self, value):
        self._setNumber(1, value)

    def getSeparatorsCount(self):
        return self._getNumber(2)

    def setSeparatorsCount(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(ContextMenuContentModel, self)._initialize()
        self._addViewModelProperty('contextMenuList', ListModel())
        self._addNumberProperty('itemsCount', 0)
        self._addNumberProperty('separatorsCount', 0)
        self.onItemClicked = self._addCommand('onItemClicked')