# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/simple_tooltip_content_model.py
from frameworks.wulf import ViewModel

class SimpleTooltipContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SimpleTooltipContentModel, self).__init__(properties=properties, commands=commands)

    def getHeader(self):
        return self._getString(0)

    def setHeader(self, value):
        self._setString(0, value)

    def getBody(self):
        return self._getString(1)

    def setBody(self, value):
        self._setString(1, value)

    def getNote(self):
        return self._getString(2)

    def setNote(self, value):
        self._setString(2, value)

    def getAlert(self):
        return self._getString(3)

    def setAlert(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(SimpleTooltipContentModel, self)._initialize()
        self._addStringProperty('header', '')
        self._addStringProperty('body', '')
        self._addStringProperty('note', '')
        self._addStringProperty('alert', '')