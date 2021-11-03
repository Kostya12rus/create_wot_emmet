# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/window_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class WindowModel(ViewModel):
    __slots__ = ('onClosed', 'onMinimized')

    def __init__(self, properties=3, commands=2):
        super(WindowModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getRawTitle(self):
        return self._getString(1)

    def setRawTitle(self, value):
        self._setString(1, value)

    def getCanMinimize(self):
        return self._getBool(2)

    def setCanMinimize(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(WindowModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addStringProperty('rawTitle', '')
        self._addBoolProperty('canMinimize', False)
        self.onClosed = self._addCommand('onClosed')
        self.onMinimized = self._addCommand('onMinimized')