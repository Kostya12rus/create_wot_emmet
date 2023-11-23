# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/descriptions_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.tutorial.view_description_model import ViewDescriptionModel

class DescriptionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(DescriptionsModel, self).__init__(properties=properties, commands=commands)

    def getViews(self):
        return self._getArray(0)

    def setViews(self, value):
        self._setArray(0, value)

    @staticmethod
    def getViewsType():
        return ViewDescriptionModel

    def _initialize(self):
        super(DescriptionsModel, self)._initialize()
        self._addArrayProperty('views', Array())