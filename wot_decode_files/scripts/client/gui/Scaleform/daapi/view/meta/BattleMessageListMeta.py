# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleMessageListMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleMessageListMeta(BaseDAAPIComponent):

    def onRefreshComplete(self):
        self._printOverrideError('onRefreshComplete')

    def as_setupListS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupList(data)

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()

    def as_refreshS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refresh()

    def as_showYellowMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showYellowMessage(key, text)

    def as_showRedMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showRedMessage(key, text)

    def as_showPurpleMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showPurpleMessage(key, text)

    def as_showGreenMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showGreenMessage(key, text)

    def as_showGoldMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showGoldMessage(key, text)

    def as_showSelfMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelfMessage(key, text)