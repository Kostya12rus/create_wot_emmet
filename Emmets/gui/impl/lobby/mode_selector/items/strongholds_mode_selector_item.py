# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/items/strongholds_mode_selector_item.py
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem
from gui.shared.ClanCache import g_clanCache

class StrongholdsModeSelectorItem(ModeSelectorLegacyItem):
    __slots__ = ()

    def _onInitializing(self):
        super(StrongholdsModeSelectorItem, self)._onInitializing()
        g_clientUpdateManager.addCallbacks({'stats.clanInfo': self.__clanInfoUpdateHandler})
        self.__resolveClanText()

    def _onDisposing(self):
        super(StrongholdsModeSelectorItem, self)._onDisposing()
        g_clientUpdateManager.removeObjectCallbacks(self)

    def __clanInfoUpdateHandler(self, *args):
        self.__resolveClanText()

    def __resolveClanText(self):
        if g_clanCache.isInClan:
            dynAcc = R.strings.mode_selector.mode.strongholdsBattlesList.call.c_2()
        else:
            dynAcc = R.strings.mode_selector.mode.strongholdsBattlesList.call.c_1()
        self.viewModel.setStatusActive(backport.text(dynAcc))