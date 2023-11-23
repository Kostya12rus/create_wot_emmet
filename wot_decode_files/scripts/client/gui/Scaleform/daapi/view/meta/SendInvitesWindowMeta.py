# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SendInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SendInvitesWindowMeta(AbstractWindowView):

    def showError(self, value):
        self._printOverrideError('showError')

    def setOnlineFlag(self, value):
        self._printOverrideError('setOnlineFlag')

    def sendInvites(self, accountsToInvite, comment):
        self._printOverrideError('sendInvites')

    def getAllAvailableContacts(self):
        self._printOverrideError('getAllAvailableContacts')

    def as_onReceiveSendInvitesCooldownS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_onReceiveSendInvitesCooldown(value)

    def as_setDefaultOnlineFlagS(self, onlineFlag):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultOnlineFlag(onlineFlag)

    def as_setInvalidUserTagsS(self, tags):
        if self._isDAAPIInited():
            return self.flashObject.as_setInvalidUserTags(tags)

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_onContactUpdatedS(self, contact):
        if self._isDAAPIInited():
            return self.flashObject.as_onContactUpdated(contact)

    def as_onListStateChangedS(self, isEmpty):
        if self._isDAAPIInited():
            return self.flashObject.as_onListStateChanged(isEmpty)

    def as_enableDescriptionS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDescription(isEnabled)

    def as_enableMassSendS(self, isEnabled, addAllTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_enableMassSend(isEnabled, addAllTooltip)