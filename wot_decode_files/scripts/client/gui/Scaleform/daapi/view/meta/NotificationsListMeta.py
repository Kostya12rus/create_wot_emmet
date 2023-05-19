# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationsListMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NotificationsListMeta(SmartPopOverView):

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def onGroupChange(self, groupIdx):
        self._printOverrideError('onGroupChange')

    def onCheckNewsClick(self):
        self._printOverrideError('onCheckNewsClick')

    def as_setInitDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setMessagesListS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagesList(value)

    def as_appendMessageS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(messageData)

    def as_updateMessageS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(messageData)

    def as_updateCountersS(self, counts):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounters(counts)

    def as_setProgressiveRewardEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressiveRewardEnabled(isEnabled)

    def as_setIsNewsBlockEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsNewsBlockEnabled(isEnabled)

    def as_setCheckNewsBtnEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckNewsBtnEnabled(isEnabled)