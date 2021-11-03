# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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