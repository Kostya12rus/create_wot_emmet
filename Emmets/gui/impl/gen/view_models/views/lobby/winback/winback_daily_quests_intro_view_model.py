# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/winback_daily_quests_intro_view_model.py
from frameworks.wulf import ViewModel

class WinbackDailyQuestsIntroViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=1, commands=1):
        super(WinbackDailyQuestsIntroViewModel, self).__init__(properties=properties, commands=commands)

    def getHasBattlePass(self):
        return self._getBool(0)

    def setHasBattlePass(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(WinbackDailyQuestsIntroViewModel, self)._initialize()
        self._addBoolProperty('hasBattlePass', False)
        self.onClose = self._addCommand('onClose')