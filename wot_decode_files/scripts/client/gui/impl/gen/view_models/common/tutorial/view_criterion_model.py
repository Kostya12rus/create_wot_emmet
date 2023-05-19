# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/view_criterion_model.py
from frameworks.wulf import ViewModel

class ViewCriterionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ViewCriterionModel, self).__init__(properties=properties, commands=commands)

    def getComponentId(self):
        return self._getString(0)

    def setComponentId(self, value):
        self._setString(0, value)

    def getViewUniqueId(self):
        return self._getString(1)

    def setViewUniqueId(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(ViewCriterionModel, self)._initialize()
        self._addStringProperty('componentId', '')
        self._addStringProperty('viewUniqueId', '')