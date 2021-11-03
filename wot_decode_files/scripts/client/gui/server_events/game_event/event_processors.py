# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/game_event/event_processors.py
import logging, BigWorld
from gui.shared.gui_items.processors import Processor
_logger = logging.getLogger(__name__)

class ChangeSelectedDifficultyLevel(Processor):

    def __init__(self, level, force=False):
        super(ChangeSelectedDifficultyLevel, self).__init__(plugins=None)
        self._level = level
        self._force = force
        return

    def _request(self, callback):
        _logger.debug('Make server request to change difficulty level -> %d', self._level)
        BigWorld.player().changeSelectedDifficultyLevel(self._level, self._force, lambda code, errorCode: self._response(code, callback, errorCode))