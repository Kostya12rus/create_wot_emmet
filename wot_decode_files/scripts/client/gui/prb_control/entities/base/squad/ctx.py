# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/squad/ctx.py
from constants import PREBATTLE_TYPE
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getWaitingID', 'waitingID'), ('getFlagsToStrings', 'flags'))
class SquadSettingsCtx(UnitRequestCtx):
    __slots__ = ('__accountsToInvite', )

    def __init__(self, entityType=PREBATTLE_TYPE.SQUAD, waitingID='', flags=prb_settings.FUNCTIONAL_FLAG.UNDEFINED, accountsToInvite=None, isForced=False):
        super(SquadSettingsCtx, self).__init__(entityType=entityType, waitingID=waitingID, flags=flags, isForced=isForced)
        self.__accountsToInvite = accountsToInvite or []

    def getRequestType(self):
        return prb_settings.REQUEST_TYPE.CREATE

    def getID(self):
        return 0

    def getAccountsToInvite(self):
        return self.__accountsToInvite