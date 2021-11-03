# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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