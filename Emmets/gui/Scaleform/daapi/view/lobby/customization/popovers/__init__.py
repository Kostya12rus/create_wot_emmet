# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/__init__.py
from collections import namedtuple
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER
ItemsGroupVO = namedtuple('ItemsGroupVO', ('userName', 'titleLabel', 'isTitle'))

class C11nPopoverItemData(object):
    __slots__ = ('item', 'season', 'slotsIds', 'isBase', 'isRemovable', 'isRemoved',
                 'isFromInventory')

    def __init__(self, item, season=None, isBase=False, isRemovable=False, isRemoved=False, isFromInventory=False):
        self.item = item
        self.season = season
        self.slotsIds = []
        self.isBase = isBase
        self.isRemovable = isRemovable
        self.isRemoved = isRemoved
        self.isFromInventory = isFromInventory


def orderKey(itemData):
    item = itemData.item
    typeOrder = TYPES_ORDER.index(item.itemTypeID)
    return (
     not itemData.isBase, itemData.isRemovable, typeOrder, item.intCD, not itemData.isFromInventory)