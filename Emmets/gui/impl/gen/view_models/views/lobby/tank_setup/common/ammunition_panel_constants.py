# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_panel_constants.py
from frameworks.wulf import ViewModel

class AmmunitionPanelConstants(ViewModel):
    __slots__ = ()
    NO_GROUP = 0
    EQUIPMENT_AND_SHELLS = 1
    OPTIONAL_DEVICES_AND_BOOSTERS = 2

    def __init__(self, properties=0, commands=0):
        super(AmmunitionPanelConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(AmmunitionPanelConstants, self)._initialize()