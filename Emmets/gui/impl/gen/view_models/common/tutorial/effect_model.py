# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/effect_model.py
from frameworks.wulf import ViewModel

class EffectModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(EffectModel, self).__init__(properties=properties, commands=commands)

    def getViewId(self):
        return self._getString(0)

    def setViewId(self, value):
        self._setString(0, value)

    def getComponentId(self):
        return self._getString(1)

    def setComponentId(self, value):
        self._setString(1, value)

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)

    def getBuilder(self):
        return self._getString(3)

    def setBuilder(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(EffectModel, self)._initialize()
        self._addStringProperty('viewId', '')
        self._addStringProperty('componentId', '')
        self._addStringProperty('type', '')
        self._addStringProperty('builder', '')