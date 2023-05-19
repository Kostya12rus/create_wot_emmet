# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/players_panel.py
from constants import ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.comp7.comp7_voip_helper import Comp7VoipHelper, VoiceChatControlTextStyles
from gui.Scaleform.daapi.view.meta.Comp7PlayersPanelMeta import Comp7PlayersPanelMeta

class PlayersPanel(Comp7PlayersPanelMeta):

    def __init__(self):
        super(PlayersPanel, self).__init__()
        self.__voipHelper = Comp7VoipHelper(component=self, textStyle=VoiceChatControlTextStyles.PLAYERS_PANEL)

    def onVoiceChatControlClick(self):
        self.__voipHelper.onVoiceChatControlClick()

    def setPeriod(self, period):
        self.__voipHelper.enable(enable=self.__isVoipControlEnabled(period))

    def _populate(self):
        super(PlayersPanel, self)._populate()
        self.__voipHelper.populate()
        self.__voipHelper.enable(enable=self.__isVoipControlEnabled())

    def _dispose(self):
        self.__voipHelper.dispose()
        super(PlayersPanel, self)._dispose()

    @classmethod
    def __isVoipControlEnabled(cls, period=None):
        if period is None:
            period = cls.sessionProvider.shared.arenaPeriod.getPeriod()
        return period == ARENA_PERIOD.PREBATTLE