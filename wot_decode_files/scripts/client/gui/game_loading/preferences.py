# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/preferences.py
import typing
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
SECTION_NAME = 'gameLoading'

class GameLoadingPreferences(object):
    __slots__ = ('_gameLoadingPrefs', )

    def __init__(self, preferences):
        super(GameLoadingPreferences, self).__init__()
        if not preferences.has_key(SECTION_NAME):
            preferences.write(SECTION_NAME, '')
        self._gameLoadingPrefs = preferences[SECTION_NAME]

    def getLoadingMax(self, slideID):
        loadingMax = self._gameLoadingPrefs[slideID]
        if loadingMax is None:
            return loadingMax
        else:
            return loadingMax.asInt

    def setLoadingMax(self, slideID, value):
        self._gameLoadingPrefs.write(slideID, value)