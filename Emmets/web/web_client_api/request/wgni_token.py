# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/wgni_token.py
from constants import TOKEN_TYPE
from gui.shared.utils.requesters import getTokenRequester
from web.web_client_api import w2c, W2CSchema

class WgniTokenWebApiMixin(object):

    @w2c(W2CSchema, 'token1')
    def wgniToken(self, cmd):
        tokenRqs = getTokenRequester(TOKEN_TYPE.WGNI)
        if not tokenRqs.isInProcess():
            response = yield tokenRqs.request(timeout=10.0)
        else:
            response = None
        if response and response.isValid():
            yield {'request_id': 'token1', 'spa_id': str(response.getDatabaseID()), 
               'token': response.getToken()}
        else:
            coolDownExpiration = tokenRqs.getReqCoolDown() - tokenRqs.lastResponseDelta()
            yield {'request_id': 'token1', 
               'error': 'Unable to obtain token.', 
               'cooldown': coolDownExpiration if coolDownExpiration > 0 else tokenRqs.getReqCoolDown()}
        return