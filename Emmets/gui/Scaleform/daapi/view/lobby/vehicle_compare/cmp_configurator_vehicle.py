# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_vehicle.py


class _CompareConfiguratorVehicle(object):
    __slots__ = ('__vehicle', )

    def __init__(self):
        super(_CompareConfiguratorVehicle, self).__init__()
        self.__vehicle = None
        return

    def setVehicle(self, value):
        self.__vehicle = value

    @property
    def item(self):
        return self.__vehicle

    def isPresent(self):
        return self.__vehicle is not None

    def clear(self):
        self.__vehicle = None
        return


g_cmpConfiguratorVehicle = _CompareConfiguratorVehicle()