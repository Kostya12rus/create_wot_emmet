# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/rect_model.py
from frameworks.wulf import ViewModel

class RectModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RectModel, self).__init__(properties=properties, commands=commands)

    def getX(self):
        return self._getNumber(0)

    def setX(self, value):
        self._setNumber(0, value)

    def getY(self):
        return self._getNumber(1)

    def setY(self, value):
        self._setNumber(1, value)

    def getWidth(self):
        return self._getNumber(2)

    def setWidth(self, value):
        self._setNumber(2, value)

    def getHeight(self):
        return self._getNumber(3)

    def setHeight(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(RectModel, self)._initialize()
        self._addNumberProperty('x', 0)
        self._addNumberProperty('y', 0)
        self._addNumberProperty('width', 0)
        self._addNumberProperty('height', 0)