# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/customization/__init__.py
from collections import namedtuple
from items.components.c11n_constants import ProjectionDecalDirectionTags
from shared_utils import first

def directionByTag(tags):
    directionTags = (tag for tag in tags if tag.startswith(ProjectionDecalDirectionTags.PREFIX))
    return first(directionTags, ProjectionDecalDirectionTags.ANY)


def isNeedToMirrorProjectionDecal(item, slot):
    if not item.canBeMirroredHorizontally:
        return False
    itemDirection = directionByTag(item.tags)
    slotDirection = directionByTag(slot.tags)
    if itemDirection == ProjectionDecalDirectionTags.ANY or slotDirection == ProjectionDecalDirectionTags.ANY:
        return False
    return itemDirection != slotDirection


CustomizationTooltipContext = namedtuple('CustomizationTooltipContext', ('itemCD',
                                                                         'vehicleIntCD',
                                                                         'showInventoryBlock',
                                                                         'level',
                                                                         'showOnlyProgressBlock'))
CustomizationTooltipContext.__new__.__defaults__ = (
 -1, -1, False, -1, False)
C11nStyleProgressData = namedtuple('C11nStyleProgressData', ('styleID', 'branch', 'level'))
C11nStyleProgressData.__new__.__defaults__ = (-1, -1, -1)