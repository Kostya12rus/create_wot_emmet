# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/BonusCaps.py
from typing import Dict, Optional, Set, FrozenSet

class BonusCapsConst(object):
    CONFIG_NAME = 'bonus_caps_override_config'
    REMOVE = 'remove'
    ADD = 'add'
    OVERRIDE = 'override'


class BonusCapsConfig(object):
    __slots__ = {
     '__config'}
    __OPERATIONS = {BonusCapsConst.REMOVE: lambda x, y: x - y, 
       BonusCapsConst.ADD: lambda x, y: x | y, 
       BonusCapsConst.OVERRIDE: lambda x, y: y}

    def __init__(self, config=None):
        if not config:
            config = dict()
        self.__config = config

    def __performOperations(self, arenaBonusType, defaultBonusCaps):
        configBonusCaps = self.__config[arenaBonusType]
        resultBonusCaps = set(defaultBonusCaps)
        for operation in configBonusCaps.iterkeys():
            resultBonusCaps = self.__OPERATIONS[operation](resultBonusCaps, configBonusCaps[operation])

        return resultBonusCaps

    def getModifiedBonusCaps(self, arenaBonusType, defaultBonusCaps):
        if self.__config.get(arenaBonusType, None) is None:
            return defaultBonusCaps
        else:
            return frozenset(self.__performOperations(arenaBonusType, defaultBonusCaps))