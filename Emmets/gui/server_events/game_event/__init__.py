# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/game_event/__init__.py
import logging
from functools import wraps
from helpers import dependency
from skeletons.gui.game_event_controller import IGameEventController
_logger = logging.getLogger(__name__)

def ifGameEventDisabled(result=None):

    def inner(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            gameEvent = dependency.instance(IGameEventController)
            if not gameEvent.isEnabled():
                _logger.debug('Event is disabled. Call %s not allowed.', function)
                return result
            return function(*args, **kwargs)

        return wrapper

    return inner