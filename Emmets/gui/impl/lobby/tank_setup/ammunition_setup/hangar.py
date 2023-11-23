# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/ammunition_setup/hangar.py
import BigWorld
from constants import QUEUE_TYPE, PREBATTLE_TYPE
from gui.impl.lobby.tank_setup.ammunition_setup.base_hangar import BaseHangarAmmunitionSetupView
from gui.impl.lobby.tank_setup.ammunition_panel.hangar import HangarAmmunitionPanel
from gui.impl.lobby.tank_setup.main_tank_setup.hangar import HangarMainTankSetupView
from gui.impl.lobby.tank_setup.tank_setup_builder import HangarTankSetupBuilder, EpicBattleTankSetupBuilder, HalloweenTankSetupBuilder

class HangarAmmunitionSetupView(BaseHangarAmmunitionSetupView):

    def __init__(self, *args, **kwargs):
        super(HangarAmmunitionSetupView, self).__init__(*args, **kwargs)
        self._isEventHangar = False

    def _onLoading(self, *args, **kwargs):
        super(HangarAmmunitionSetupView, self)._onLoading(*args, **kwargs)
        self._isEventHangar = self._hwController.isEventHangar()
        if self._isEventHangar:
            self._hwController.onEventDisabled += self._onEventDisabled
            self._hwController.onCompleteActivePhase += self._onCompleteActivePhase

    def _finalize(self):
        if self._isEventHangar:
            self._hwController.onEventDisabled -= self._onEventDisabled
            self._hwController.onCompleteActivePhase -= self._onCompleteActivePhase
        super(HangarAmmunitionSetupView, self)._finalize()

    def _createMainTankSetup(self):
        return HangarMainTankSetupView(self.viewModel.tankSetup, self.__getTankSetupBuilder()(self._vehItem))

    def _createAmmunitionPanel(self):
        ctx = {'specializationClickable': True}
        return HangarAmmunitionPanel(self.viewModel.ammunitionPanel, self._vehItem.getItem(), ctx=ctx)

    def _onCompleteActivePhase(self):
        if self._hwController.isPostPhase():
            self.__closeWindow()

    def _onEventDisabled(self):
        self.__closeWindow()

    def __closeWindow(self):
        if self.viewModel.getIsReady():
            self._forceCloseWindow()

    def __getTankSetupBuilder(self):
        if self.prbDispatcher is not None and self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.EPIC) or self.prbDispatcher.getFunctionalState().isInUnit(PREBATTLE_TYPE.EPIC):
            return EpicBattleTankSetupBuilder
        hwEqCtrl = BigWorld.player().components.get('HWAccountEquipmentController', None)
        if self.prbDispatcher is not None and hwEqCtrl is not None and (self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.HALLOWEEN_BATTLES) or self.prbDispatcher.getFunctionalState().isInUnit(PREBATTLE_TYPE.HALLOWEEN_BATTLES) or self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.HALLOWEEN_BATTLES_WHEEL)):
            return HalloweenTankSetupBuilder
        return HangarTankSetupBuilder