# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/game_event_getter.py
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class GameEventGetterMixin(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        self.__gameEventStorage = None
        return

    @property
    def storage(self):
        storage = self.__gameEventStorage
        if not storage:
            componentSystem = self.sessionProvider.arenaVisitor.getComponentSystem()
            self.__gameEventStorage = storage = getattr(componentSystem, 'gameEventComponent', None)
        return storage

    @property
    def scenarioAnimationTriggers(self):
        return self.storage.scenarioAnimationTriggers()

    @property
    def souls(self):
        return self.storage.getSouls()

    @property
    def soulCollector(self):
        return self.storage.getSoulCollector()

    @property
    def damageData(self):
        return self.storage.getDamageData()

    @property
    def blockedDamageData(self):
        return self.storage.getBlockedDamageData()

    @property
    def teammateResurrectEquipment(self):
        return self.storage.getTeammateResurrectEquipment()

    @property
    def enemySpottedData(self):
        return self.storage.getEnemySpottedData()

    @property
    def environmentData(self):
        return self.storage.getEnvironmentData()

    @property
    def bossFightData(self):
        return self.storage.getBossFightData()

    @property
    def ecpState(self):
        return self.storage.ecpState

    @property
    def nearbyIndicatorData(self):
        return self.storage.getNearbyIndicator()