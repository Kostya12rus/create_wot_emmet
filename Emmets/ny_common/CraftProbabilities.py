# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ny_common/CraftProbabilities.py
from typing import Tuple
from ny_common.settings import CraftProbsConsts

class CraftProbabilitiesConfig(object):
    __slots__ = ('_config', )

    def __init__(self, config=None):
        self._config = config or {}

    def getProbabilitiesForTypes(self):
        return self._config.get(CraftProbsConsts.TYPE_PROBABILITIES, ())

    def getProbabilitiesForSettings(self):
        return self._config.get(CraftProbsConsts.SETTING_PROBABILITIES, ())

    def getProbabilitiesForRanks(self):
        return self._config.get(CraftProbsConsts.RANK_PROBABILITIES, ())