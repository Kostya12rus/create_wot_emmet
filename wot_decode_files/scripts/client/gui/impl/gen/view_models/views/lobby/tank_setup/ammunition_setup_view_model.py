# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/ammunition_setup_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_model import AmmunitionPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_action_model import TankSetupActionModel

class AmmunitionSetupViewModel(ViewModel):
    __slots__ = ('onClose', 'onResized', 'onViewRendered', 'onAnimationEnd')

    def __init__(self, properties=8, commands=4):
        super(AmmunitionSetupViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def tankSetup(self):
        return self._getViewModel(0)

    @property
    def ammunitionPanel(self):
        return self._getViewModel(1)

    @property
    def lastSlotAction(self):
        return self._getViewModel(2)

    @property
    def vehicleInfo(self):
        return self._getViewModel(3)

    def getShow(self):
        return self._getBool(4)

    def setShow(self, value):
        self._setBool(4, value)

    def getIsReady(self):
        return self._getBool(5)

    def setIsReady(self, value):
        self._setBool(5, value)

    def getIsBootcamp(self):
        return self._getBool(6)

    def setIsBootcamp(self, value):
        self._setBool(6, value)

    def getIsEvent(self):
        return self._getBool(7)

    def setIsEvent(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(AmmunitionSetupViewModel, self)._initialize()
        self._addViewModelProperty('tankSetup', MainTankSetupModel())
        self._addViewModelProperty('ammunitionPanel', AmmunitionPanelModel())
        self._addViewModelProperty('lastSlotAction', TankSetupActionModel())
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addBoolProperty('show', False)
        self._addBoolProperty('isReady', False)
        self._addBoolProperty('isBootcamp', False)
        self._addBoolProperty('isEvent', False)
        self.onClose = self._addCommand('onClose')
        self.onResized = self._addCommand('onResized')
        self.onViewRendered = self._addCommand('onViewRendered')
        self.onAnimationEnd = self._addCommand('onAnimationEnd')