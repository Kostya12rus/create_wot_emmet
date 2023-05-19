# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/tooltips/collection_item_tooltip_view_model.py
from frameworks.wulf import ViewModel

class CollectionItemTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CollectionItemTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)

    def getIsReceived(self):
        return self._getBool(2)

    def setIsReceived(self, value):
        self._setBool(2, value)

    def getImagePath(self):
        return self._getString(3)

    def setImagePath(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(CollectionItemTooltipViewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('description', '')
        self._addBoolProperty('isReceived', False)
        self._addStringProperty('imagePath', '')