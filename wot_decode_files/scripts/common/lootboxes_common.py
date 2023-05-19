# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/lootboxes_common.py
from constants import LOOTBOX_TOKEN_PREFIX
from soft_exception import SoftException

def makeLootboxTokenID(boxID):
    return LOOTBOX_TOKEN_PREFIX + str(boxID)


def makeLootboxID(tokenName):
    try:
        if tokenName.startswith(LOOTBOX_TOKEN_PREFIX):
            strID = tokenName[len(LOOTBOX_TOKEN_PREFIX):]
            return int(strID)
    except Exception:
        pass

    raise SoftException(('Invalid tokenName: {}').format(tokenName))


def isLootboxToken(tokenName):
    try:
        makeLootboxID(tokenName)
        return True
    except Exception:
        return False