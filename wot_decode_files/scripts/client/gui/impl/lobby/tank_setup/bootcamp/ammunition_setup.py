# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/bootcamp/ammunition_setup.py
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import BaseHangarAmmunitionSetupView
from gui.impl.lobby.tank_setup.bootcamp.ammunition_panel import BootcampAmmunitionPanel
from gui.impl.lobby.tank_setup.bootcamp.setup_builder import BootcampTankSetupBuilder
from gui.impl.lobby.tank_setup.main_tank_setup.base import MainTankSetupView

class BootcampAmmunitionSetupView(BaseHangarAmmunitionSetupView):

    def _onLoading(self, **kwargs):
        super(BootcampAmmunitionSetupView, self)._onLoading(**kwargs)
        self.viewModel.setIsBootcamp(True)

    def _createMainTankSetup(self):
        return MainTankSetupView(self.viewModel.tankSetup, BootcampTankSetupBuilder(self._vehItem))

    def _createAmmunitionPanel(self):
        return BootcampAmmunitionPanel(self.viewModel.ammunitionPanel, self._vehItem.getItem())