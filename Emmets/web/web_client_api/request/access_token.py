# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/access_token.py
from helpers import dependency, time_utils
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.web import IWebController
from web.web_client_api import w2c, W2CSchema, Field

class _RequestAccessTokenSchema(W2CSchema):
    force = Field(required=False, type=bool)


class AccessTokenWebApiMixin(object):
    _connectionMgr = dependency.descriptor(IConnectionManager)
    _webCtrl = dependency.descriptor(IWebController)

    @w2c(_RequestAccessTokenSchema, 'access_token')
    def accessToken(self, cmd):
        accessTokenData = yield self._webCtrl.getAccessTokenData(force=cmd.force)
        if accessTokenData is not None:
            yield {'spa_id': str(self._connectionMgr.databaseID), 'access_token': str(accessTokenData.accessToken), 
               'expires_in': accessTokenData.expiresAt - time_utils.getCurrentTimestamp(), 
               'periphery_id': str(self._connectionMgr.peripheryID)}
        else:
            yield {'error': 'Unable to obtain access token.'}
        return