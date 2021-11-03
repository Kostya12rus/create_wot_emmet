# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/triggers_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class TriggersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TriggersModel, self).__init__(properties=properties, commands=commands)

    def getComponentId(self):
        return self._getString(0)

    def setComponentId(self, value):
        self._setString(0, value)

    def getTriggers(self):
        return self._getArray(1)

    def setTriggers(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(TriggersModel, self)._initialize()
        self._addStringProperty('componentId', '')
        self._addArrayProperty('triggers', Array())