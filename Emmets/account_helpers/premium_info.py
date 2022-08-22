# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/premium_info.py
from constants import PREMIUM_TYPE

class PremiumInfo(object):

    def __init__(self):
        self._rawPremiumInfo = {p:0 for p in PREMIUM_TYPE.TYPES_SORTED}
        self._rawPremiumInfo['premMask'] = 0

    def update(self, rawPremiumInfo):
        self._rawPremiumInfo.update(rawPremiumInfo)

    def isActivePremium(self, checkPremiumType):
        return self.activePremiumType >= checkPremiumType

    @property
    def isPremium(self):
        return self.activePremiumType != PREMIUM_TYPE.NONE

    @property
    def totalPremiumExpiryTime(self):
        premiumMask = self._rawPremiumInfo['premMask']
        return max(tuple(self._rawPremiumInfo[p] for p in PREMIUM_TYPE.TYPES_SORTED if bool(premiumMask & p)) + (0, ))

    @property
    def activePremiumExpiryTime(self):
        activePremiumType = self.activePremiumType
        if activePremiumType != PREMIUM_TYPE.NONE:
            return self._rawPremiumInfo[activePremiumType]
        return 0

    @property
    def activePremiumType(self):
        return PREMIUM_TYPE.activePremium(self._rawPremiumInfo['premMask'])

    @property
    def data(self):
        premiumMask = self._rawPremiumInfo['premMask']
        return {pType:{'active': bool(premiumMask & pType), 'expiryTime': self._rawPremiumInfo[pType]} for pType in PREMIUM_TYPE.TYPES_SORTED}