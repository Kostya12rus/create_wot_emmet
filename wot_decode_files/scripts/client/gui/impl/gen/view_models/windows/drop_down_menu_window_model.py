# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/drop_down_menu_window_model.py
from frameworks.wulf import ViewModel

class DropDownMenuWindowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DropDownMenuWindowModel, self).__init__(properties=properties, commands=commands)

    def getX(self):
        return self._getReal(0)

    def setX(self, value):
        self._setReal(0, value)

    def getY(self):
        return self._getReal(1)

    def setY(self, value):
        self._setReal(1, value)

    def getTargetWidth(self):
        return self._getReal(2)

    def setTargetWidth(self, value):
        self._setReal(2, value)

    def getTargetHeight(self):
        return self._getReal(3)

    def setTargetHeight(self, value):
        self._setReal(3, value)

    def _initialize(self):
        super(DropDownMenuWindowModel, self)._initialize()
        self._addRealProperty('x', 0.0)
        self._addRealProperty('y', 0.0)
        self._addRealProperty('targetWidth', 0.0)
        self._addRealProperty('targetHeight', 0.0)