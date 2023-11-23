# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/banner_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.season_model import SeasonModel

class State(IntEnum):
    NOTSTARTED = 0
    JUSTSTARTED = 1
    ACTIVE = 2
    ENDSOON = 3
    END = 4
    DISABLED = 5


class BannerModel(ViewModel):
    __slots__ = ('onOpen', )

    def __init__(self, properties=4, commands=1):
        super(BannerModel, self).__init__(properties=properties, commands=commands)

    @property
    def season(self):
        return self._getViewModel(0)

    @staticmethod
    def getSeasonType():
        return SeasonModel

    def getState(self):
        return State(self._getNumber(1))

    def setState(self, value):
        self._setNumber(1, value.value)

    def getIsSingle(self):
        return self._getBool(2)

    def setIsSingle(self, value):
        self._setBool(2, value)

    def getTimeLeftUntilPrimeTime(self):
        return self._getNumber(3)

    def setTimeLeftUntilPrimeTime(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(BannerModel, self)._initialize()
        self._addViewModelProperty('season', SeasonModel())
        self._addNumberProperty('state')
        self._addBoolProperty('isSingle', True)
        self._addNumberProperty('timeLeftUntilPrimeTime', 0)
        self.onOpen = self._addCommand('onOpen')