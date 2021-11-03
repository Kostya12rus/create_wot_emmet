# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TabbedFullStatsMeta.py
from gui.Scaleform.daapi.view.battle.classic.base_stats import StatsBase

class TabbedFullStatsMeta(StatsBase):

    def onSelectQuest(self, questID):
        self._printOverrideError('onSelectQuest')

    def as_setActiveTabS(self, tabIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setActiveTab(tabIndex)

    def as_questProgressPerformS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_questProgressPerform(data)

    def as_resetActiveTabS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetActiveTab()

    def as_updateProgressTrackingS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressTracking(data)

    def as_updateTabsS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTabs(dataProvider)