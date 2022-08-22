# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/uilogging/__init__.py
from helpers import dependency
from skeletons.ui_logging import IUILoggingCore
from uilogging.core.core_constants import LogLevels
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _UILoggingLogSchema(W2CSchema):
    feature = Field(required=True, type=basestring)
    group = Field(required=True, type=basestring)
    log_action = Field(required=True, type=basestring)
    log_level = Field(required=False, type=int, default=LogLevels.INFO)
    params = Field(required=False, type=dict, default={})


@w2capi(name='ui_logging', key='action')
class UILoggingWebApi(object):
    _logger = dependency.descriptor(IUILoggingCore)

    @w2c(_UILoggingLogSchema, 'log')
    def log(self, cmd):
        self._logger.log(feature=cmd.feature, group=cmd.group, action=cmd.log_action, loglevel=cmd.log_level, **cmd.params)