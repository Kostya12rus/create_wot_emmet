# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/collections_constants.py
from collections_common import COLLECTIONS_PREFIX
COLLECTION_ITEM_BONUS_NAME = 'collectionItem'
COLLECTION_ITEM_PREFIX_NAME = COLLECTIONS_PREFIX + '_item'
COLLECTION_ITEM_TOKEN_PREFIX_NAME = 'cllc:item:'
COLLECTION_ITEM_RES_KEY_TEMPLATE = '{}_{}_{}'
COLLECTION_RES_PREFIX = 'collection_'
COLLECTION_START_EVENT_TYPE = 'collectionStart'
COLLECTION_START_SEEN = 'collectionStartNotification'

def cllcTokenToEntitlement(tokenID):
    try:
        _, _, collectionId, itemId = tokenID.split(':')
        return COLLECTION_ITEM_PREFIX_NAME + ('_{}_{}').format(collectionId, itemId)
    except ValueError:
        return

    return