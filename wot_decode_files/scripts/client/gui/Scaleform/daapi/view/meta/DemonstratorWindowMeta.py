# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DemonstratorWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class DemonstratorWindowMeta(AbstractWindowView):

    def onGameplaySelected(self, index):
        self._printOverrideError('onGameplaySelected')

    def onLvlSelected(self, index):
        self._printOverrideError('onLvlSelected')

    def onSpawnSelected(self, index):
        self._printOverrideError('onSpawnSelected')

    def onMapSelected(self, index):
        self._printOverrideError('onMapSelected')

    def onBattleStart(self):
        self._printOverrideError('onBattleStart')

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_setGameplayTabsS(self, tabList, selectedTab):
        if self._isDAAPIInited():
            return self.flashObject.as_setGameplayTabs(tabList, selectedTab)

    def as_setSpawnsS(self, spawnList, selectedSpawn):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpawns(spawnList, selectedSpawn)

    def as_setLevelsS(self, lvlList, selectedLvl):
        if self._isDAAPIInited():
            return self.flashObject.as_setLevels(lvlList, selectedLvl)

    def as_enablePlatoonWarningS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enablePlatoonWarning(value)

    def as_enableExtendedSettingsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableExtendedSettings(value)

    def as_enableBattleButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableBattleButton(value)