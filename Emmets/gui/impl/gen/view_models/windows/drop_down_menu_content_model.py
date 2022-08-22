# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/drop_down_menu_content_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class DropDownMenuContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DropDownMenuContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def dropDownList(self):
        return self._getViewModel(0)

    @staticmethod
    def getDropDownListType():
        return ListModel

    def getListItemRenderer(self):
        return self._getString(1)

    def setListItemRenderer(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DropDownMenuContentModel, self)._initialize()
        self._addViewModelProperty('dropDownList', ListModel())
        self._addStringProperty('listItemRenderer', '')