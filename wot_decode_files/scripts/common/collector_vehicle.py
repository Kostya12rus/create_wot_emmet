# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/collector_vehicle.py


class CollectorVehicleConsts(object):
    CONFIG_NAME = 'collector_vehicle_config'
    COLLECTOR_VEHICLES_TAG = 'collectorVehicle'
    COLLECTOR_MEDAL_PREFIX = 'collectorVehicle'
    IS_ENABLED = 'enabled'


class CollectorVehicleConfig(object):
    __slots__ = ('__config', )

    def __init__(self, config):
        self.__config = config

    @property
    def isEnabled(self):
        return self.__config.get(CollectorVehicleConsts.IS_ENABLED, False)