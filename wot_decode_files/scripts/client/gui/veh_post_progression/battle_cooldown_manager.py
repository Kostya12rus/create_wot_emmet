# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_post_progression/battle_cooldown_manager.py
from gui.shared.rq_cooldown import RequestCooldownManager, REQUEST_SCOPE

class BattleCooldownManager(RequestCooldownManager):

    def __init__(self, default=0.5):
        super(BattleCooldownManager, self).__init__(REQUEST_SCOPE.BATTLE_ACTION)
        self.__default = default

    def lookupName(self, rqTypeID):
        return ''

    def getDefaultCoolDown(self):
        return self.__default

    def _showSysMessage(self, msg):
        pass