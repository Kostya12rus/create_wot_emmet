# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/qualification_battle.py
from enum import Enum
from frameworks.wulf import ViewModel

class BattleState(Enum):
    NOTPLAYED = 'notPlayed'
    INPROGRESS = 'inProgress'
    VICTORY = 'victory'
    DEFEAT = 'defeat'


class QualificationBattle(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(QualificationBattle, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return BattleState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(QualificationBattle, self)._initialize()
        self._addStringProperty('state')