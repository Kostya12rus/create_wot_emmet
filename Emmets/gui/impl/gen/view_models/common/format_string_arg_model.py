# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/format_string_arg_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class FormatStringArgModel(ViewModel):
    __slots__ = ()
    ALIGN_LEFT = 'left'
    ALIGN_RIGHT = 'right'
    ALIGN_CENTER = 'center'

    def __init__(self, properties=5, commands=0):
        super(FormatStringArgModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getStyle(self):
        return self._getResource(2)

    def setStyle(self, value):
        self._setResource(2, value)

    def getAlign(self):
        return self._getString(3)

    def setAlign(self, value):
        self._setString(3, value)

    def getHardSpace(self):
        return self._getBool(4)

    def setHardSpace(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(FormatStringArgModel, self)._initialize()
        self._addStringProperty('value', '')
        self._addStringProperty('name', '')
        self._addResourceProperty('style', R.invalid())
        self._addStringProperty('align', 'left')
        self._addBoolProperty('hardSpace', False)