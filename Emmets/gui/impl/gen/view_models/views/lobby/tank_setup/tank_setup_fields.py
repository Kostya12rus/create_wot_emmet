# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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