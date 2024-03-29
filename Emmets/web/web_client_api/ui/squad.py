# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/squad.py
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from web.web_client_api import w2c, W2CSchema, Field
from web.web_client_api.common import SPA_ID_TYPES

class _CreateSquadSchema(W2CSchema):
    spa_id = Field(required=True, type=SPA_ID_TYPES)


class SquadWebApiMixin(object):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @w2c(_CreateSquadSchema, 'squad_window')
    def createSquad(self, usersIds):
        yield self.prbDispatcher.doSelectAction(PrbAction(PREBATTLE_ACTION_NAME.SQUAD, accountsToInvite=(usersIds.spa_id,)))