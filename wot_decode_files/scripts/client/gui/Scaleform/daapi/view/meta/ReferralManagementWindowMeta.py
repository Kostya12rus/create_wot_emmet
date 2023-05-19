# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReferralManagementWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReferralManagementWindowMeta(AbstractWindowView):

    def onInvitesManagementLinkClick(self):
        self._printOverrideError('onInvitesManagementLinkClick')

    def inviteIntoSquad(self, referralID):
        self._printOverrideError('inviteIntoSquad')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTableDataS(self, referrals):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableData(referrals)

    def as_setAwardDataDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardDataData(data)

    def as_setProgressDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressData(data)

    def as_showAlertS(self, alertStr):
        if self._isDAAPIInited():
            return self.flashObject.as_showAlert(alertStr)