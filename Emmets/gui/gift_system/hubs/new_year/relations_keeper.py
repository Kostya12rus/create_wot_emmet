# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/new_year/relations_keeper.py
from gui.gift_system.hubs.base.relations_keeper import GiftEventBaseKeeper
from gui.gift_system.hubs.base.relations_keeper import IGiftEventKeeper

class IGiftEventNYKeeper(IGiftEventKeeper):

    def isFullfilled(self, spaID):
        raise NotImplementedError


class GiftEventNYKeeper(GiftEventBaseKeeper, IGiftEventNYKeeper):
    __slots__ = ()

    def isFullfilled(self, spaID):
        outcomeRelations = self.getOutcomeRelations(implicitCopy=False)
        return spaID in outcomeRelations and outcomeRelations[spaID]