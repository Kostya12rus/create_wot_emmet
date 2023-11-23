# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleStatisticDataControllerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleStatisticDataControllerMeta(BaseDAAPIComponent):

    def onRefreshComplete(self):
        self._printOverrideError('onRefreshComplete')

    def as_refreshS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refresh()

    def as_resetFragsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFrags()

    def as_setVehiclesDataS(self, vehData):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesData(vehData)

    def as_addVehiclesInfoS(self, vehInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_addVehiclesInfo(vehInfo)

    def as_updateVehiclesInfoS(self, upVehInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehiclesInfo(upVehInfo)

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)

    def as_setFragsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFrags(data)

    def as_updateVehiclesStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehiclesStats(data)

    def as_updatePlayerStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerStatus(data)

    def as_setArenaInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setArenaInfo(data)

    def as_setQuestStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setQuestStatus(data)

    def as_setUserTagsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setUserTags(data)

    def as_updateUserTagsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateUserTags(data)

    def as_updateInvitationsStatusesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInvitationsStatuses(data)

    def as_setPersonalStatusS(self, bitmask):
        if self._isDAAPIInited():
            return self.flashObject.as_setPersonalStatus(bitmask)

    def as_updatePersonalStatusS(self, added=0, removed=0):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePersonalStatus(added, removed)

    def as_setQuestsInfoS(self, data, setForce):
        if self._isDAAPIInited():
            return self.flashObject.as_setQuestsInfo(data, setForce)

    def as_updateQuestProgressS(self, condID, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestProgress(condID, data)

    def as_updateQuestHeaderProgressS(self, headerProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestHeaderProgress(headerProgress)

    def as_updateTriggeredChatCommandsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTriggeredChatCommands(data)