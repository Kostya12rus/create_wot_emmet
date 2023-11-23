# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/regular_achvs.py
from abstract import RegularAchievement
from abstract.mixins import NoProgressBar
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements import validators

class Achieved(RegularAchievement):
    __slots__ = ()

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)


class HonoredRankAchievement(RegularAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(HonoredRankAchievement, self).__init__('honoredRank', _AB.CLIENT, dossier, value)

    def getIcons(self):
        iconName = self._getIconName()
        return {self.ICON_TYPE.IT_180X180: '%s/%s.png' % (self.ICON_PATH_180X180, iconName), 
           self.ICON_TYPE.IT_67X71: '%s/%s.png' % (self.ICON_PATH_67X71, iconName)}

    @classmethod
    def checkIsInDossier(cls, block, name, dossier):
        if dossier is not None:
            return bool(cls.__getCount(dossier))
        else:
            return False

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return True

    def _readValue(self, dossier):
        return self.__getCount(dossier)

    @classmethod
    def __getCount(cls, dossier):
        return dossier.getRankedStats().getTotalRanksCount()


class MoonSphereAchievement(RegularAchievement, NoProgressBar):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MoonSphereAchievement, self).__init__('moonSphere', _AB.SINGLE, dossier, value)

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)


class ReferralProgramSingleAchievement(RegularAchievement):
    __slots__ = ()

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.requiresReferralProgram() or validators.alreadyAchieved(cls, name, block, dossier)