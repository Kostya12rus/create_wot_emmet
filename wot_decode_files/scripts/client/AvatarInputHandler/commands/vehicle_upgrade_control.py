# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/vehicle_upgrade_control.py
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
import CommandMapping
from gui.battle_control import event_dispatcher

class VehicleUpdateControl(InputHandlerCommand):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        progressionCtrl = self.__guiSessionProvider.dynamic.progression
        if progressionCtrl and progressionCtrl.isVehicleReady():
            if isDown and CommandMapping.g_instance.isFired(CommandMapping.CMD_UPGRADE_PANEL_SHOW, key):
                event_dispatcher.showBattleVehicleConfigurator()
                event_dispatcher.toggleFullStats(False)
                return True
        return False


class VehicleUpgradePanelControl(InputHandlerCommand):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        progressionCtrl = self.__guiSessionProvider.dynamic.progression
        if progressionCtrl:
            if isDown and CommandMapping.g_instance.isFiredList([
             CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_LEFT,
             CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_ALTERNATIVE_LEFT], key):
                progressionCtrl.selectVehicleModule(0)
                return True
            if isDown and CommandMapping.g_instance.isFiredList([
             CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_RIGHT,
             CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_ALTERNATIVE_RIGHT], key):
                progressionCtrl.selectVehicleModule(1)
                return True
        return False