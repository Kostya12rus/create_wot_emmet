# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/session_stats_button.py
from gui.Scaleform.daapi.view.meta.ButtonWithCounterMeta import ButtonWithCounterMeta
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from constants import ARENA_BONUS_TYPE

class SessionStatsButton(ButtonWithCounterMeta):
    _itemsCache = dependency.descriptor(IItemsCache)

    def _populate(self):
        super(SessionStatsButton, self)._populate()
        self._itemsCache.onSyncCompleted += self.__updateSessionStatButton
        self.__updateBatteleCount()

    def _dispose(self):
        self._itemsCache.onSyncCompleted -= self.__updateSessionStatButton
        super(SessionStatsButton, self)._dispose()

    def __updateBatteleCount(self):
        battleCnt = self._itemsCache.items.sessionStats.getAccountStats(ARENA_BONUS_TYPE.REGULAR).battleCnt
        self.as_setCountS(battleCnt)

    def __updateSessionStatButton(self, *_):
        self.__updateBatteleCount()