# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/MapsTrainingStorageComponent.py
import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from maps_training_common.maps_training_constants import VEHICLE_CLASSES_ORDER

class MapsTrainingStorageComponent(BigWorld.DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(MapsTrainingStorageComponent, self).__init__()
        self._globalGoalsData = {k:0 for k in VEHICLE_CLASSES_ORDER}

    def getGlobalGoal(self, key):
        return self._globalGoalsData[key]

    def set_localGoal(self, *args, **kwargs):
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onLocalKillGoalsUpdated(self.localGoal)
        return

    def set_globalGoals(self, *args, **kwargs):
        for vehClass, newValue in zip(VEHICLE_CLASSES_ORDER, self.globalGoals):
            prevValue = self._globalGoalsData[vehClass]
            self._globalGoalsData[vehClass] = newValue
            ctrl = self.sessionProvider.shared.feedback
            if ctrl is not None and newValue < prevValue:
                ctrl.destroyGoal(vehClass)

        return