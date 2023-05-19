# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_option_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectOptionViewModel(ViewModel):
    __slots__ = ('onClicked', )

    def __init__(self, properties=3, commands=1):
        super(SelectOptionViewModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getItemsType():
        return SelectOptionBaseItemViewModel

    def getSelectedIndexes(self):
        return self._getArray(1)

    def setSelectedIndexes(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSelectedIndexesType():
        return int

    def getMessage(self):
        return self._getString(2)

    def setMessage(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(SelectOptionViewModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self._addArrayProperty('selectedIndexes', Array())
        self._addStringProperty('message', '')
        self.onClicked = self._addCommand('onClicked')