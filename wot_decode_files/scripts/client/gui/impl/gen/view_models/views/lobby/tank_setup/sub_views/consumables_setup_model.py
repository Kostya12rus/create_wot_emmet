# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/consumables_setup_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel

class ConsumablesSetupModel(BaseSetupModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=7):
        super(ConsumablesSetupModel, self).__init__(properties=properties, commands=commands)

    def getTempString(self):
        return self._getString(5)

    def setTempString(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(ConsumablesSetupModel, self)._initialize()
        self._addStringProperty('tempString', '')