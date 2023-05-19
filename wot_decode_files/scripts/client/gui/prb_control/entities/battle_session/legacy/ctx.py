# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/ctx.py
from gui.prb_control.entities.base.legacy.ctx import JoinLegacyCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getID', 'prbID'), ('getPrbTypeName', 'type'), ('getWaitingID',
                                                                          'waitingID'))
class JoinBattleSessionCtx(JoinLegacyCtx):
    __slots__ = ()

    def __init__(self, prbID, prbType, waitingID='', flags=FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinBattleSessionCtx, self).__init__(prbID, prbType, waitingID=waitingID, flags=flags)