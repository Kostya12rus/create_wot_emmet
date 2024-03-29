# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/slot_label_element_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class Types(Enum):
    IMAGE = 'image'
    TEXT = 'text'


class SlotLabelElementModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SlotLabelElementModel, self).__init__(properties=properties, commands=commands)

    def getContent(self):
        return self._getString(0)

    def setContent(self, value):
        self._setString(0, value)

    def getType(self):
        return Types(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)

    def getStyleJson(self):
        return self._getString(2)

    def setStyleJson(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(SlotLabelElementModel, self)._initialize()
        self._addStringProperty('content', '')
        self._addStringProperty('type')
        self._addStringProperty('styleJson', '')