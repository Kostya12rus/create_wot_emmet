# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_vehicle.py
from CurrentVehicle import g_currentVehicle
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class _TankSetupVehicle(object):
    __slots__ = ('__vehicle', )
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(_TankSetupVehicle, self).__init__()
        self.__vehicle = None
        return

    def setVehicle(self, value):
        self.__vehicle = value

    @property
    def item(self):
        return self.__vehicle or g_currentVehicle.item

    @property
    def defaultItem(self):
        if g_currentVehicle.isPresent():
            return g_currentVehicle.item
        else:
            return

    def isPresent(self):
        return self.__vehicle is not None

    def dispose(self):
        self.__vehicle = None
        return


g_tankSetupVehicle = _TankSetupVehicle()