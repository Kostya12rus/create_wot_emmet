# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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