# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/Comp7PlayersPanelMeta.py
from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class Comp7PlayersPanelMeta(PlayersPanel):

    def onVoiceChatControlClick(self):
        self._printOverrideError('onVoiceChatControlClick')

    def as_setVoiceChatDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatData(data)

    def as_setVoiceChatControlVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatControlVisible(value)

    def as_setVoiceChatControlSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatControlSelected(value)