# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/battle_royale.py
import vehicles
SPAWNED_TAG_NAME = 'spawned'
BATTLE_ROYALE_TAG_NAME = 'battle_royale'

def isSpawnedBot(vehicleTags):
    return SPAWNED_TAG_NAME in vehicleTags


def isBattleRoyale(vehicleTags):
    return BATTLE_ROYALE_TAG_NAME in vehicleTags


class ModulesInstaller(object):
    _UNLOCKS_START_INDEX = 2

    @classmethod
    def checkModuleValidity(self, intCD, vehicleDescriptor):
        module = vehicles.getItemByCompactDescr(intCD)
        vehicleModules = (
         vehicleDescriptor.chassis,
         vehicleDescriptor.turret,
         vehicleDescriptor.gun,
         vehicleDescriptor.engine,
         vehicleDescriptor.radio)
        currentLevel = module.level
        previousLevel = currentLevel - 1
        if not all(module.level < currentLevel for module in vehicleModules):
            return (False, 'invalid module level')
        else:
            if previousLevel > 1:
                for previousModule in vehicleModules:
                    if previousModule.level == previousLevel and previousModule.unlocks:
                        unlocksDescrs = vehicleDescriptor.type.unlocksDescrs
                        for modulesData in unlocksDescrs:
                            modulesDataLen = len(modulesData)
                            if modulesDataLen > self._UNLOCKS_START_INDEX:
                                moduleCD = modulesData[1]
                                if moduleCD == intCD:
                                    i = self._UNLOCKS_START_INDEX
                                    while i < modulesDataLen:
                                        if modulesData[i] == previousModule.compactDescr:
                                            return (
                                             True, None)
                                        i = i + 1

                return (
                 False, 'module is not in unlocks')
            return (
             True, None)

    @classmethod
    def getItemsThisModuleUnlocks(self, targetIntCD, vehicleDescriptor):
        outcome = []
        unlocksDescrs = vehicleDescriptor.type.unlocksDescrs
        for modulesData in unlocksDescrs:
            modulesDataLen = len(modulesData)
            if modulesDataLen > self._UNLOCKS_START_INDEX:
                targetModuleLevel = vehicles.getItemByCompactDescr(targetIntCD).level
                unlockedIntCD = modulesData[1]
                i = self._UNLOCKS_START_INDEX
                while i < modulesDataLen:
                    unlockIntCD = modulesData[i]
                    if unlockIntCD == targetIntCD:
                        if targetModuleLevel == vehicles.getItemByCompactDescr(unlockedIntCD).level:
                            outcome.append(unlockedIntCD)
                        break
                    i = i + 1

        return tuple(outcome)