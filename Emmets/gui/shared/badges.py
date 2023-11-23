# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/badges.py
from gui.doc_loaders.badges_loader import getAvailableBadges
from helpers import dependency
from skeletons.gui.shared.gui_items import IGuiItemsFactory

def buildBadge(badgeID, extraData=None):
    if badgeID != 0:
        allBadges = getAvailableBadges()
        badgeDescriptor = allBadges[badgeID].copy()
        if badgeDescriptor is not None:
            return dependency.instance(IGuiItemsFactory).createBadge(badgeDescriptor, extraData=extraData)
    return