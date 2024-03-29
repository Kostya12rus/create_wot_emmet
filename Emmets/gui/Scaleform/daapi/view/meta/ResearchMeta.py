# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchMeta.py
from gui.Scaleform.daapi.view.lobby.techtree.research_view import ResearchView

class ResearchMeta(ResearchView):

    def requestResearchData(self):
        self._printOverrideError('requestResearchData')

    def request4Unlock(self, itemCD, topLevel):
        self._printOverrideError('request4Unlock')

    def request4Rent(self, itemCD):
        self._printOverrideError('request4Rent')

    def goToNextVehicle(self, vehCD):
        self._printOverrideError('goToNextVehicle')

    def exitFromResearch(self):
        self._printOverrideError('exitFromResearch')

    def goToVehicleView(self, itemCD):
        self._printOverrideError('goToVehicleView')

    def compareVehicle(self, itemCD):
        self._printOverrideError('compareVehicle')

    def onModuleHover(self, id):
        self._printOverrideError('onModuleHover')

    def goToPostProgression(self, itemCD):
        self._printOverrideError('goToPostProgression')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setRootDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRootData(data)

    def as_setResearchItemsS(self, nation, raw):
        if self._isDAAPIInited():
            return self.flashObject.as_setResearchItems(nation, raw)

    def as_setFreeXPS(self, freeXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setFreeXP(freeXP)

    def as_setInstalledItemsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInstalledItems(data)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)

    def as_setXpInfoLinkageS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setXpInfoLinkage(linkage)

    def as_setPostProgressionDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostProgressionData(data)

    def as_showPostProgressionUnlockAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showPostProgressionUnlockAnimation()