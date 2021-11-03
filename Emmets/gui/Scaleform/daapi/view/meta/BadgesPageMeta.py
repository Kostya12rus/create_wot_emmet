# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BadgesPageMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class BadgesPageMeta(WrapperViewMeta):

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onSelectBadge(self, badgeID):
        self._printOverrideError('onSelectBadge')

    def onDeselectBadge(self):
        self._printOverrideError('onDeselectBadge')

    def onSelectSuffixBadge(self, badgeID):
        self._printOverrideError('onSelectSuffixBadge')

    def onDeselectSuffixBadge(self):
        self._printOverrideError('onDeselectSuffixBadge')

    def onDummyButtonPress(self):
        self._printOverrideError('onDummyButtonPress')

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setReceivedBadgesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivedBadges(data)

    def as_setNotReceivedBadgesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotReceivedBadges(data)

    def as_setSelectedBadgeS(self, data, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedBadge(data, selected)

    def as_setBadgeSuffixS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBadgeSuffix(data)