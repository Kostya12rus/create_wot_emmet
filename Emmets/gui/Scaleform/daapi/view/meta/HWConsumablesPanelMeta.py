# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/HWConsumablesPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel

class HWConsumablesPanelMeta(ConsumablesPanel):

    def as_setShellInfinityS(self, idx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShellInfinity(idx, value)

    def as_addAbilitySlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addAbilitySlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText)

    def as_updateAbilityS(self, idx, stage, count, timeRemaining, maxTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAbility(idx, stage, count, timeRemaining, maxTime)

    def as_addPassiveAbilitySlotS(self, idx, iconPath, state, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addPassiveAbilitySlot(idx, iconPath, state, tooltipText)

    def as_updatePassiveAbilityS(self, idx, state, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePassiveAbility(idx, state, tooltipText)

    def as_resetPassiveAbilitiesS(self, slots=None):
        if self._isDAAPIInited():
            return self.flashObject.as_resetPassiveAbilities(slots)