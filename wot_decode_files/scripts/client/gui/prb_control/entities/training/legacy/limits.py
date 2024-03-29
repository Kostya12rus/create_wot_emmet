# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/limits.py
from CurrentVehicle import g_currentVehicle
from constants import PREBATTLE_ACCOUNT_STATE, PREBATTLE_TYPE
from gui.prb_control.entities.base.limits import AbstractTeamIsValid, LimitsCollection, VehicleIsValid
from gui.prb_control.entities.base.limits import TeamNoPlayersInBattle, TeamIsValid
from gui.prb_control.settings import PREBATTLE_RESTRICTION
from helpers import dependency
from items import vehicles
from skeletons.gui.shared import IItemsCache

class ObserverInTeamIsValid(AbstractTeamIsValid):
    itemsCache = dependency.descriptor(IItemsCache)

    def check(self, rosters, team, teamLimits):
        accountsInfo = self._getAccountsInfo(rosters, team)
        if len(accountsInfo) < teamLimits['minCount']:
            return (False, 'limit/minCount')
        if self.__isAllObservers(accountsInfo):
            return (False, 'observers')
        return (
         True, '')

    @classmethod
    def __isAllObservers(cls, accountsInfo):
        if not accountsInfo:
            return False
        for accInfo in accountsInfo.itervalues():
            if not accInfo['state'] & PREBATTLE_ACCOUNT_STATE.READY:
                continue
            if 'vehTypeCompDescr' not in accInfo or 'vehLevel' not in accInfo:
                vehDescr = vehicles.VehicleDescr(compactDescr=accInfo['vehCompDescr'])
                vehTypeCompDescr = vehDescr.type.compactDescr
            else:
                vehTypeCompDescr = accInfo['vehTypeCompDescr']
            if not cls.itemsCache.items.getItemByCD(vehTypeCompDescr).isObserver:
                return False

        return True


class TrainingVehicleIsValid(VehicleIsValid):

    def check(self, teamLimits):
        isValid, restriction = super(TrainingVehicleIsValid, self).check(teamLimits)
        if isValid and g_currentVehicle.isObserver():
            return (False, PREBATTLE_RESTRICTION.VEHICLE_NOT_SUPPORTED)
        return (isValid, restriction)


class TrainingLimits(LimitsCollection):

    def __init__(self, entity):
        super(TrainingLimits, self).__init__(entity, (
         TrainingVehicleIsValid(),), (
         TeamNoPlayersInBattle(PREBATTLE_TYPE.TRAINING),
         TeamIsValid(),
         ObserverInTeamIsValid()))