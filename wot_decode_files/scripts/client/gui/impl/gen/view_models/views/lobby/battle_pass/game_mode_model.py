# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/game_mode_model.py
from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_card_model import GameModeCardModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel

class ArenaBonusType(IntEnum):
    REGULAR = 1
    RANKED = 22
    BATTLE_ROYALE_SOLO = 29
    EPIC_BATTLE = 27
    COMP7 = 43


class GameModeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(GameModeModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)

    def getArenaBonusType(self):
        return ArenaBonusType(self._getNumber(2))

    def setArenaBonusType(self, value):
        self._setNumber(2, value.value)

    def getTableRows(self):
        return self._getArray(3)

    def setTableRows(self, value):
        self._setArray(3, value)

    @staticmethod
    def getTableRowsType():
        return GameModeRowsModel

    def getCards(self):
        return self._getArray(4)

    def setCards(self, value):
        self._setArray(4, value)

    @staticmethod
    def getCardsType():
        return GameModeCardModel

    def _initialize(self):
        super(GameModeModel, self)._initialize()
        self._addStringProperty('title', '')
        self._addStringProperty('text', '')
        self._addNumberProperty('arenaBonusType')
        self._addArrayProperty('tableRows', Array())
        self._addArrayProperty('cards', Array())