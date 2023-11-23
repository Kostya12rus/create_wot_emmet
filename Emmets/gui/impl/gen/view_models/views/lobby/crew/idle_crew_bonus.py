# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/idle_crew_bonus.py
from enum import Enum
from frameworks.wulf import ViewModel

class IdleCrewBonusEnum(Enum):
    DISABLED = 'Disabled'
    ENABLED = 'Enabled'
    ACTIVEONCURRENTVEHICLE = 'ActiveOnCurrentVehicle'
    INCOMPATIBLEWITHCURRENTVEHICLE = 'IncompatibleWithCurrentVehicle'
    ACTIVEONANOTHERVEHICLE = 'ActiveOnAnotherVehicle'
    INVISIBLE = 'Invisible'


class IdleCrewBonus(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(IdleCrewBonus, self).__init__(properties=properties, commands=commands)

    def getIdleCrewBonus(self):
        return IdleCrewBonusEnum(self._getString(0))

    def setIdleCrewBonus(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(IdleCrewBonus, self)._initialize()
        self._addStringProperty('IdleCrewBonus')