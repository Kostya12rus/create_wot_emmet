# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/recruit_window/drop_down_item_view_model.py
from frameworks.wulf import ViewModel

class DropDownItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DropDownItemViewModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DropDownItemViewModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('label', '')