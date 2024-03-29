# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dt_dog_tag.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_component import DtComponent

class DtDogTag(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DtDogTag, self).__init__(properties=properties, commands=commands)

    @property
    def engraving(self):
        return self._getViewModel(0)

    @staticmethod
    def getEngravingType():
        return DtComponent

    @property
    def background(self):
        return self._getViewModel(1)

    @staticmethod
    def getBackgroundType():
        return DtComponent

    def getPlayerName(self):
        return self._getString(2)

    def setPlayerName(self, value):
        self._setString(2, value)

    def getClanTag(self):
        return self._getString(3)

    def setClanTag(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(DtDogTag, self)._initialize()
        self._addViewModelProperty('engraving', DtComponent())
        self._addViewModelProperty('background', DtComponent())
        self._addStringProperty('playerName', '')
        self._addStringProperty('clanTag', '')