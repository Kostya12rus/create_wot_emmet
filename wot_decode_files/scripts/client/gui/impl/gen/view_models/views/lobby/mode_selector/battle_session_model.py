# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/battle_session_model.py
from frameworks.wulf import ViewModel

class BattleSessionModel(ViewModel):
    __slots__ = ('onTournamentsClicked', 'onGlobalMapClicked', 'onClanClicked', 'onCloseClicked')

    def __init__(self, properties=4, commands=4):
        super(BattleSessionModel, self).__init__(properties=properties, commands=commands)

    def getIsInClan(self):
        return self._getBool(0)

    def setIsInClan(self, value):
        self._setBool(0, value)

    def getClanName(self):
        return self._getString(1)

    def setClanName(self, value):
        self._setString(1, value)

    def getClanIcon(self):
        return self._getString(2)

    def setClanIcon(self, value):
        self._setString(2, value)

    def getIsTournamentLinkIGB(self):
        return self._getBool(3)

    def setIsTournamentLinkIGB(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(BattleSessionModel, self)._initialize()
        self._addBoolProperty('isInClan', False)
        self._addStringProperty('clanName', '')
        self._addStringProperty('clanIcon', '')
        self._addBoolProperty('isTournamentLinkIGB', False)
        self.onTournamentsClicked = self._addCommand('onTournamentsClicked')
        self.onGlobalMapClicked = self._addCommand('onGlobalMapClicked')
        self.onClanClicked = self._addCommand('onClanClicked')
        self.onCloseClicked = self._addCommand('onCloseClicked')