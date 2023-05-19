# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/battle_pass/__init__.py
from helpers import dependency
from helpers.events_handler import EventsHandler
from skeletons.gui.game_control import IBattlePassController
from web.client_web_api.api import C2WHandler, c2w
from web.common import formatBattlePassInfo

class BattlePassEventHandler(C2WHandler, EventsHandler):
    __battlePass = dependency.descriptor(IBattlePassController)

    def init(self):
        super(BattlePassEventHandler, self).init()
        self._subscribe()

    def fini(self):
        self._unsubscribe()
        super(BattlePassEventHandler, self).fini()

    def _getEvents(self):
        return (
         (
          self.__battlePass.onBattlePassIsBought, self.__sendInfo),
         (
          self.__battlePass.onSeasonStateChanged, self.__sendInfo),
         (
          self.__battlePass.onBattlePassSettingsChange, self.__sendInfo),
         (
          self.__battlePass.onChapterChanged, self.__sendInfo))

    @c2w(name='battle_pass_info_changed')
    def __sendInfo(self, *args, **kwargs):
        return formatBattlePassInfo()