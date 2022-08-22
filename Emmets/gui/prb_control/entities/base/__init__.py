# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/__init__.py
from adisp import process
from gui.shared.utils import functions
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

def vehicleAmmoCheck(func):
    from CurrentVehicle import g_currentVehicle

    @process
    def wrapper(*args, **kwargs):
        res = yield functions.checkAmmoLevel((g_currentVehicle.item,))
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper


def lobbyHeaderNavigationPossibleCheck(func):

    @process
    def wrapper(*args, **kwargs):
        lobbyContext = dependency.instance(ILobbyContext)
        res = yield lobbyContext.isHeaderNavigationPossible()
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper


@process
def checkVehicleAmmoFull(vehicle, callback):
    res = yield functions.checkAmmoLevel((vehicle,))
    if res:
        callback()