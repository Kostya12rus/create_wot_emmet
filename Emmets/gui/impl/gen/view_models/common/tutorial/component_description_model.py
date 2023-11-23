# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/component_description_model.py
from frameworks.wulf import ViewModel

class ComponentDescriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ComponentDescriptionModel, self).__init__(properties=properties, commands=commands)

    def getViewId(self):
        return self._getString(0)

    def setViewId(self, value):
        self._setString(0, value)

    def getComponentId(self):
        return self._getString(1)

    def setComponentId(self, value):
        self._setString(1, value)

    def getPath(self):
        return self._getString(2)

    def setPath(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(ComponentDescriptionModel, self)._initialize()
        self._addStringProperty('viewId', '')
        self._addStringProperty('componentId', '')
        self._addStringProperty('path', '')