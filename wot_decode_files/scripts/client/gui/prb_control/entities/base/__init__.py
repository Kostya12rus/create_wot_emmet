# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/__init__.py
from adisp import adisp_process
from gui.shared.utils import functions
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

def vehicleAmmoCheck(func):
    from CurrentVehicle import g_currentVehicle

    @adisp_process
    def wrapper(*args, **kwargs):
        res = yield functions.checkAmmoLevel((g_currentVehicle.item,))
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper


def lobbyHeaderNavigationPossibleCheck(func):

    @adisp_process
    def wrapper(*args, **kwargs):
        lobbyContext = dependency.instance(ILobbyContext)
        res = yield lobbyContext.isHeaderNavigationPossible()
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper


@adisp_process
def checkVehicleAmmoFull(vehicle, callback):
    res = yield functions.checkAmmoLevel((vehicle,))
    if res:
        callback()