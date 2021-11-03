# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventHeaderMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventHeaderMeta(BaseDAAPIComponent):

    def menuItemClick(self, alias):
        self._printOverrideError('menuItemClick')

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_setCoinsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoins(value)

    def as_setDifficultyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDifficulty(value)

    def as_setScreenS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setScreen(alias)

    def as_setHangarMenuDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHangarMenuData(data)

    def as_setButtonCounterS(self, btnAlias, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonCounter(btnAlias, value)

    def as_removeButtonCounterS(self, btnAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_removeButtonCounter(btnAlias)