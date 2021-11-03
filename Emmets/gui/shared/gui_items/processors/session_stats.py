# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/processors/session_stats.py
import logging, BigWorld
from gui.shared.gui_items.processors import Processor, makeI18nError
_logger = logging.getLogger(__name__)

class ResetSessionStatsProcessor(Processor):

    def _errorHandler(self, code, errStr='', ctx=None):
        defaultKey = 'session_stats/reset/server_error'
        return makeI18nError(('/').join((defaultKey, errStr)), defaultKey)

    def _request(self, callback):
        _logger.debug('Make server request to reset session stats')
        BigWorld.player().sessionStats.resetStats(lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr))