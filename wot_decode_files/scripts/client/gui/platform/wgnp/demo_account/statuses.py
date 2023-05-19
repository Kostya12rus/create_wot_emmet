# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/demo_account/statuses.py
import typing
from constants import EMAIL_CONFIRMATION_TOKEN_NAME
from gui.platform.base.response import Codes
from gui.platform.base.statuses.constants import StatusTypes
from gui.platform.base.statuses.status import Status
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.platform.wgnp.demo_account.request import CredentialsStatusParams

class DemoAccCredentialsStatus(Status):
    __slots__ = ()

    @property
    def isSpaWeakPassword(self):
        return self.data.get('error', '') == 'spa_weak_password'

    @property
    def login(self):
        return self.data.get('login', '')


class DemoAccNicknameStatus(Status):
    __slots__ = ()

    @property
    def cost(self):
        return self.data.get('cost', '')


def createCredentialsConfirmationStatus():
    itemsCache = dependency.instance(IItemsCache)
    statusType = StatusTypes.CONFIRMATION_SENT
    if itemsCache.items.tokens.isTokenAvailable(EMAIL_CONFIRMATION_TOKEN_NAME):
        statusType = StatusTypes.CONFIRMED
    return DemoAccCredentialsStatus(statusType=statusType)


def createCredentialStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        state, login = response.getData().get('state'), response.getData().get('login', '')
        if state in ('no_active_request', 'spa_login_already_taken'):
            statusType = StatusTypes.ADD_NEEDED
        elif state == 'email_sent':
            statusType, data = StatusTypes.ADDED, {'login': login}
        if state == 'spa_generic_conflict':
            data = None
        else:
            if state == 'spa_weak_password':
                statusType, data = StatusTypes.ADD_NEEDED, {'error': 'spa_weak_password', 'login': login}
            else:
                return createCredentialsConfirmationStatus()
    else:
        data = {'error': Codes(response.code)}
    return DemoAccCredentialsStatus(statusType=statusType, data=data)


def createNicknameStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        extras = response.getData().get('extras', {})
        errors = response.getData().get('errors', {}).get('__all__', [])
        cost = extras.get('free', '')
        if extras.get('available', False):
            if cost == 'demo_free_first_renaming':
                statusType, data = StatusTypes.ADD_NEEDED, {'cost': cost}
            else:
                statusType = StatusTypes.ADDED
        else:
            if 'incomplete_state' in errors:
                statusType = StatusTypes.PROCESSING
            else:
                data = response.getData()
    else:
        data = {'error': Codes(response.code)}
    return DemoAccNicknameStatus(statusType=statusType, data=data)