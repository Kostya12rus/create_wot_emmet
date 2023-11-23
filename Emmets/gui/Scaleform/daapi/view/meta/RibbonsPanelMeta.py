# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RibbonsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RibbonsPanelMeta(BaseDAAPIComponent):

    def onShow(self, ribbonId):
        self._printOverrideError('onShow')

    def onChange(self):
        self._printOverrideError('onChange')

    def onHide(self, ribbonId):
        self._printOverrideError('onHide')

    def as_setupS(self, items, isExtendedAnim, isVisible, isWithRibbonName, isWithVehName, bonusLabels):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(items, isExtendedAnim, isVisible, isWithRibbonName, isWithVehName, bonusLabels)

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()

    def as_addBattleEfficiencyEventS(self, ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role):
        if self._isDAAPIInited():
            return self.flashObject.as_addBattleEfficiencyEvent(ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role)

    def as_updateBattleEfficiencyEventS(self, ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleEfficiencyEvent(ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role)

    def as_setSettingsS(self, isVisible, isExtendedAnim, isWithRibbonName, isWithVehName):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(isVisible, isExtendedAnim, isWithRibbonName, isWithVehName)