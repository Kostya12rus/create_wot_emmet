# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/regular_ext_achvs.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularExtAchievement
from abstract.mixins import NoProgressBar
from arena_achievements import ACHIEVEMENT_CONDITIONS, ACHIEVEMENT_CONDITIONS_EXT

class HeroesOfRassenayAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, 'heroesOfRassenay', _AB.TOTAL, dossier, value)

    def _getStandardValues(self):
        return ACHIEVEMENT_CONDITIONS[self._getActualName()]['minKills']

    def _getExtValues(self):
        return ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['minKills']


class MedalLafayettePoolAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, 'medalLafayettePool', _AB.TOTAL, dossier, value)

    def _getStandardValues(self):
        return str(ACHIEVEMENT_CONDITIONS[self._getActualName()]['minKills']) + '-' + str(ACHIEVEMENT_CONDITIONS[self._getActualName()]['maxKills'])

    def _getExtValues(self):
        return str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['minKills']) + '-' + str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['maxKills'])


class MedalRadleyWaltersAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, 'medalRadleyWalters', _AB.TOTAL, dossier, value)

    def _getStandardValues(self):
        return str(ACHIEVEMENT_CONDITIONS[self._getActualName()]['minKills']) + '-' + str(ACHIEVEMENT_CONDITIONS[self._getActualName()]['maxKills'])

    def _getExtValues(self):
        return str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['minKills']) + '-' + str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['maxKills'])


class WarriorAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, 'warrior', _AB.TOTAL, dossier, value)

    def _getStandardValues(self):
        return ACHIEVEMENT_CONDITIONS[self._getActualName()]['minFrags']

    def _getExtValues(self):
        return ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['minFrags']