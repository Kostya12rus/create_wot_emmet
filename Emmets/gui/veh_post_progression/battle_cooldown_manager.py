# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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