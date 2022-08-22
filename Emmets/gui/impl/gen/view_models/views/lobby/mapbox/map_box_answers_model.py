# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_answers_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class MapBoxAnswersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MapBoxAnswersModel, self).__init__(properties=properties, commands=commands)

    def getIsMultipleChoice(self):
        return self._getBool(0)

    def setIsMultipleChoice(self, value):
        self._setBool(0, value)

    def getVariants(self):
        return self._getArray(1)

    def setVariants(self, value):
        self._setArray(1, value)

    @staticmethod
    def getVariantsType():
        return str

    def getSelectedVariants(self):
        return self._getArray(2)

    def setSelectedVariants(self, value):
        self._setArray(2, value)

    @staticmethod
    def getSelectedVariantsType():
        return str

    def _initialize(self):
        super(MapBoxAnswersModel, self)._initialize()
        self._addBoolProperty('isMultipleChoice', False)
        self._addArrayProperty('variants', Array())
        self._addArrayProperty('selectedVariants', Array())