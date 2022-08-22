# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/drr_scale_ctrl.py
import weakref, BigWorld, Keys
from Event import Event
from account_helpers.settings_core.settings_constants import GRAPHICS
from gui import g_repeatKeyHandlers
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController
from helpers import dependency
from helpers import drr_scale
from skeletons.account_helpers.settings_core import ISettingsCore

class DRRScaleController(IBattleController):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, messages):
        super(DRRScaleController, self).__init__()
        self.__messages = weakref.proxy(messages)
        self.onDRRChanged = Event()

    def getControllerID(self):
        return BATTLE_CTRL_ID.DRR_SCALE

    def startControl(self):
        g_repeatKeyHandlers.add(self.__handleRepeatKeyEvent)

    def stopControl(self):
        self.__messages = None
        g_repeatKeyHandlers.discard(self.__handleRepeatKeyEvent)
        return

    def handleKey(self, key, isDown):
        if key in (Keys.KEY_MINUS, Keys.KEY_NUMPADMINUS) and BigWorld.isKeyDown(Keys.KEY_RSHIFT) and isDown and not self.settingsCore.getSetting(GRAPHICS.DRR_AUTOSCALER_ENABLED):
            result = drr_scale.stepDown()
            if result is not None and self.__messages:
                self.__messages.showVehicleMessage('DRR_SCALE_STEP_DOWN', {'scale': drr_scale.getPercent(result)})
                self.onDRRChanged()
            return True
        if key in (Keys.KEY_EQUALS, Keys.KEY_ADD) and BigWorld.isKeyDown(Keys.KEY_RSHIFT) and isDown and not self.settingsCore.getSetting(GRAPHICS.DRR_AUTOSCALER_ENABLED):
            result = drr_scale.stepUp()
            if result is not None and self.__messages:
                self.__messages.showVehicleMessage('DRR_SCALE_STEP_UP', {'scale': drr_scale.getPercent(result)})
                self.onDRRChanged()
            return True
        return False

    def __handleRepeatKeyEvent(self, event):
        self.handleKey(event.key, event.isKeyDown())