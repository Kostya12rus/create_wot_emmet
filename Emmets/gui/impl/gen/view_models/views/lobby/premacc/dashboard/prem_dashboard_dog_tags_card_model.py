# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/prem_dashboard_dog_tags_card_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.counter_model import CounterModel

class PremDashboardDogTagsCardModel(ViewModel):
    __slots__ = ('onGoToDogTagsView', )

    def __init__(self, properties=5, commands=1):
        super(PremDashboardDogTagsCardModel, self).__init__(properties=properties, commands=commands)

    @property
    def Counter(self):
        return self._getViewModel(0)

    @staticmethod
    def getCounterType():
        return CounterModel

    def getIsAvailable(self):
        return self._getBool(1)

    def setIsAvailable(self, value):
        self._setBool(1, value)

    def getIsMaxLevel(self):
        return self._getBool(2)

    def setIsMaxLevel(self, value):
        self._setBool(2, value)

    def getBackground(self):
        return self._getString(3)

    def setBackground(self, value):
        self._setString(3, value)

    def getEngraving(self):
        return self._getString(4)

    def setEngraving(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(PremDashboardDogTagsCardModel, self)._initialize()
        self._addViewModelProperty('Counter', CounterModel())
        self._addBoolProperty('isAvailable', True)
        self._addBoolProperty('isMaxLevel', False)
        self._addStringProperty('background', '')
        self._addStringProperty('engraving', '')
        self.onGoToDogTagsView = self._addCommand('onGoToDogTagsView')