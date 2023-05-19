# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/sales/triggers.py
import BigWorld
from CurrentVehicle import g_currentVehicle
from tutorial.control.triggers import Trigger, TriggerWithValidateVar
__all__ = ('TimerTrigger', 'IsCollectibleVehicleTrigger')

class TimerTrigger(TriggerWithValidateVar):

    def __init__(self, triggerID, validateVarID, setVarID=None, validateUpdateOnly=False):
        super(TimerTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self.__timerCallback = None
        return

    def run(self):
        self.isRunning = True
        if self.__timerCallback is None:
            self.isSubscribed = True
            self.__timerCallback = BigWorld.callback(self.getVar(), self.__updateTimer)
        self.toggle(isOn=False)
        return

    def clear(self):
        if self.__timerCallback is not None:
            BigWorld.cancelCallback(self.__timerCallback)
            self.__timerCallback = None
        self.isSubscribed = False
        self.isRunning = False
        return

    def __updateTimer(self, *args):
        self.__timerCallback = None
        self.toggle(isOn=True)
        return


class IsCollectibleVehicleTrigger(Trigger):

    def run(self):
        g_currentVehicle.onChanged += self.__onCurrentVehicleChanged
        self.toggle(isOn=self.isOn())

    def isOn(self, *args):
        return g_currentVehicle.isCollectible()

    def clear(self):
        g_currentVehicle.onChanged -= self.__onCurrentVehicleChanged

    def __onCurrentVehicleChanged(self):
        self.toggle(isOn=self.isOn())