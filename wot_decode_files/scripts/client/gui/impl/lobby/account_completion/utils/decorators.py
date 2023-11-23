# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/utils/decorators.py
from functools import wraps
from wg_async import wg_async, wg_await, delay
from helpers import dependency
from skeletons.gui.game_control import IOverlayController
_WAITING_DELAY = 0.001

def waitShowOverlay(func):

    @wraps(func)
    @wg_async
    def _wrapper(*args, **kwargs):
        overlay = dependency.instance(IOverlayController)
        yield wg_await(overlay.waitShow())
        yield wg_await(delay(_WAITING_DELAY))
        func(*args, **kwargs)

    return _wrapper