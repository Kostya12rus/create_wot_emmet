# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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