# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/VoiceChatManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VoiceChatManagerMeta(BaseDAAPIComponent):

    def isPlayerSpeaking(self, accountDBID):
        self._printOverrideError('isPlayerSpeaking')

    def isVivox(self):
        self._printOverrideError('isVivox')

    def isYY(self):
        self._printOverrideError('isYY')

    def isVOIPEnabled(self):
        self._printOverrideError('isVOIPEnabled')

    def isVOIPAvailable(self):
        self._printOverrideError('isVOIPAvailable')

    def as_onPlayerSpeakS(self, accountDBID, isSpeak, isHimseljoinUnitButtonf):
        if self._isDAAPIInited():
            return self.flashObject.as_onPlayerSpeak(accountDBID, isSpeak, isHimseljoinUnitButtonf)