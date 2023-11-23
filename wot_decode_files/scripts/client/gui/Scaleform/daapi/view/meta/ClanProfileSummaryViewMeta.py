# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileSummaryViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfileSummaryViewMeta(ClanProfileBaseView):

    def hyperLinkGotoMap(self):
        self._printOverrideError('hyperLinkGotoMap')

    def hyperLinkGotoDetailsMap(self):
        self._printOverrideError('hyperLinkGotoDetailsMap')

    def sendRequestHandler(self):
        self._printOverrideError('sendRequestHandler')

    def as_updateStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStatus(data)

    def as_updateGeneralBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneralBlock(data)

    def as_updateFortBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFortBlock(data)

    def as_updateGlobalMapBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGlobalMapBlock(data)

    def as_updateLeaguesBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLeaguesBlock(data)