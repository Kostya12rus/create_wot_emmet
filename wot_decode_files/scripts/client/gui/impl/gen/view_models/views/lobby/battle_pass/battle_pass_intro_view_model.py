# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_intro_view_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.base_intro_view_model import BaseIntroViewModel

class BattlePassIntroViewModel(BaseIntroViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=3):
        super(BattlePassIntroViewModel, self).__init__(properties=properties, commands=commands)

    def getBackground(self):
        return self._getResource(5)

    def setBackground(self, value):
        self._setResource(5, value)

    def _initialize(self):
        super(BattlePassIntroViewModel, self)._initialize()
        self._addResourceProperty('background', R.invalid())