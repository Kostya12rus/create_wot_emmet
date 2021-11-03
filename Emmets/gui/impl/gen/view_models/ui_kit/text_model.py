# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/text_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class TextModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TextModel, self).__init__(properties=properties, commands=commands)

    def getRawLabel(self):
        return self._getString(0)

    def setRawLabel(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(TextModel, self)._initialize()
        self._addStringProperty('rawLabel', '')
        self._addResourceProperty('label', R.invalid())
        self._addBoolProperty('isEnabled', False)