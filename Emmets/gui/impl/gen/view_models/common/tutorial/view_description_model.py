# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/view_description_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.tutorial.component_description_model import ComponentDescriptionModel

class ViewDescriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ViewDescriptionModel, self).__init__(properties=properties, commands=commands)

    def getViewId(self):
        return self._getString(0)

    def setViewId(self, value):
        self._setString(0, value)

    def getComponents(self):
        return self._getArray(1)

    def setComponents(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(ViewDescriptionModel, self)._initialize()
        self._addStringProperty('viewId', '')
        self._addArrayProperty('components', Array())