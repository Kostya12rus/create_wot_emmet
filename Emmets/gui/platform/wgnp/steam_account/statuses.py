# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/steam_account/statuses.py
import typing
from gui.platform.base.response import Codes
from gui.platform.base.statuses.constants import StatusTypes
from gui.platform.base.statuses.status import Status
if typing.TYPE_CHECKING:
    from gui.platform.wgnp.steam_account.request import EmailStatusParams

class SteamAccEmailStatus(Status):
    __slots__ = ()

    @property
    def email(self):
        return self.data.get('email', '')


def createEmailStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        state = response.getData().get('state')
        if state in ('no_active_request', 'spa_email_already_taken', 'confirmation_code_expired'):
            statusType = StatusTypes.ADD_NEEDED
        elif state == 'email_sent':
            statusType, data = StatusTypes.ADDED, {'email': response.getData().get('email', '')}
        elif state == 'spa_generic_conflict':
            data = {'error': 'spa_generic_conflict'}
        else:
            statusType = StatusTypes.CONFIRMED
    else:
        data = {'error': Codes(response.code)}
    return SteamAccEmailStatus(statusType=statusType, data=data)