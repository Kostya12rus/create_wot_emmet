# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/spa_id.py
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
from web.web_client_api import w2c, W2CSchema

class SpaIdWebApiMixin(object):
    connectionMgr = dependency.descriptor(IConnectionManager)

    @w2c(W2CSchema, 'spa_id')
    def spaId(self, cmd):
        if self.connectionMgr is not None:
            yield {'spa_id': str(self.connectionMgr.databaseID)}
        else:
            yield {'error': 'Unable to obtain spa id'}
        return