# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):

    def setVehicleModule(self, newId, oldId, isRemove):
        self._printOverrideError('setVehicleModule')

    def upgradeVehicleModule(self, moduleId):
        self._printOverrideError('upgradeVehicleModule')

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def setAutoRearm(self, autoRearm):
        self._printOverrideError('setAutoRearm')

    def buyVehicleModule(self, moduleId):
        self._printOverrideError('buyVehicleModule')

    def setCurrentTab(self, tabIndex):
        self._printOverrideError('setCurrentTab')

    def listOverlayClosed(self):
        self._printOverrideError('listOverlayClosed')

    def onManageBattleAbilitiesClicked(self):
        self._printOverrideError('onManageBattleAbilitiesClicked')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)