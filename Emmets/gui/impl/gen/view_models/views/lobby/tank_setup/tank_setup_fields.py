# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/tank_setup_fields.py
from frameworks.wulf import ViewModel

class TankSetupFields(ViewModel):
    __slots__ = ()
    TANK_SETUP_CARD = 0
    AMMO_PANEL_SLOT = 1

    def __init__(self, properties=0, commands=0):
        super(TankSetupFields, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TankSetupFields, self)._initialize()