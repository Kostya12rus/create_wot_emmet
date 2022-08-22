# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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