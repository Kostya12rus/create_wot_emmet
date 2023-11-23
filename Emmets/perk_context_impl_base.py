# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/perk_context_impl_base.py
from visual_script.misc import ASPECT

class PerkContextImplBase(object):

    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID):
        self._perksController = perksControllerWeakRef
        self._perkLevel = perkLevel
        self.perkID = perkID
        self.scopeID = scopeID
        self.vehicleID = perksControllerWeakRef.vehicleID

    @property
    def vehicle(self):
        raise NotImplementedError

    @property
    def perkLevel(self):
        raise NotImplementedError

    @perkLevel.setter
    def perkLevel(self, value):
        raise NotImplementedError

    def addFactorModifier(self, factor, value):
        raise NotImplementedError

    def removeFactorModifiers(self, factor, numMods):
        raise NotImplementedError

    def dropAllPerkModifiers(self):
        raise NotImplementedError

    def notifyOnClient(self, *_):
        raise NotImplementedError

    def notifyOnClientRibbon(self, *_):
        raise NotImplementedError


class CrewContextImplBase(PerkContextImplBase):
    ASPECT = ASPECT.ALL

    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID, tmanIdxs):
        super(PerkContextImplBase).__init__(perksControllerWeakRef, perkID, perkLevel, scopeID)
        self._levelOverride = False
        self._tmanIdxs = tmanIdxs