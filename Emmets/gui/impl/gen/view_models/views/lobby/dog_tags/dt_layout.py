# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dt_layout.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_component_layout import DtComponentLayout

class DtLayout(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(DtLayout, self).__init__(properties=properties, commands=commands)

    @property
    def playerName(self):
        return self._getViewModel(0)

    @staticmethod
    def getPlayerNameType():
        return DtComponentLayout

    @property
    def clanTag(self):
        return self._getViewModel(1)

    @staticmethod
    def getClanTagType():
        return DtComponentLayout

    @property
    def engraving(self):
        return self._getViewModel(2)

    @staticmethod
    def getEngravingType():
        return DtComponentLayout

    @property
    def inscription(self):
        return self._getViewModel(3)

    @staticmethod
    def getInscriptionType():
        return DtComponentLayout

    @property
    def statTracker(self):
        return self._getViewModel(4)

    @staticmethod
    def getStatTrackerType():
        return DtComponentLayout

    @property
    def background(self):
        return self._getViewModel(5)

    @staticmethod
    def getBackgroundType():
        return DtComponentLayout

    def _initialize(self):
        super(DtLayout, self)._initialize()
        self._addViewModelProperty('playerName', DtComponentLayout())
        self._addViewModelProperty('clanTag', DtComponentLayout())
        self._addViewModelProperty('engraving', DtComponentLayout())
        self._addViewModelProperty('inscription', DtComponentLayout())
        self._addViewModelProperty('statTracker', DtComponentLayout())
        self._addViewModelProperty('background', DtComponentLayout())