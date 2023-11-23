# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PerksPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PerksPanelMeta(BaseDAAPIComponent):

    def as_setPerksS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_setPerks(items)

    def as_updatePerkS(self, perkName, state, duration, lifeTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePerk(perkName, state, duration, lifeTime)

    def as_clearPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearPanel()