# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/dynamic_tooltip_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class DynamicTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DynamicTooltipModel, self).__init__(properties=properties, commands=commands)

    def getHeader(self):
        return self._getResource(0)

    def setHeader(self, value):
        self._setResource(0, value)

    def getBody(self):
        return self._getResource(1)

    def setBody(self, value):
        self._setResource(1, value)

    def getContentId(self):
        return self._getNumber(2)

    def setContentId(self, value):
        self._setNumber(2, value)

    def getTargetId(self):
        return self._getNumber(3)

    def setTargetId(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(DynamicTooltipModel, self)._initialize()
        self._addResourceProperty('header', R.invalid())
        self._addResourceProperty('body', R.invalid())
        self._addNumberProperty('contentId', 0)
        self._addNumberProperty('targetId', 0)