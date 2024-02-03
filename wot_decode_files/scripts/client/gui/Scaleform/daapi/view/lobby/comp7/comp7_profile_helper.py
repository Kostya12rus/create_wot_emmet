# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/comp7/comp7_profile_helper.py
COMP7_SEASON_NUMBERS = (1, 2)
COMP7_ARCHIVE_NAMES = ('Griffin', )
COMP7_ARCHIVE_DROPDOWN_KEY_PREFIX = 'comp7_archive_'
COMP7_SEASON_DROPDOWN_KEY_PREFIX = 'comp7_season_'

def isComp7Archive(battleType):
    return battleType.startswith(COMP7_ARCHIVE_DROPDOWN_KEY_PREFIX)


def isComp7Season(battleType):
    return battleType.startswith(COMP7_SEASON_DROPDOWN_KEY_PREFIX)


def getArchiveName(battleType):
    _, __, archiveName = battleType.rpartition(COMP7_ARCHIVE_DROPDOWN_KEY_PREFIX)
    return archiveName


def getSeasonName(battleType):
    _, __, seasonName = battleType.rpartition(COMP7_SEASON_DROPDOWN_KEY_PREFIX)
    return seasonName


def getDropdownKeyByArchiveName(archiveName):
    return ('{}{}').format(COMP7_ARCHIVE_DROPDOWN_KEY_PREFIX, archiveName)


def getDropdownKeyBySeason(season):
    return ('{}{}').format(COMP7_SEASON_DROPDOWN_KEY_PREFIX, season)