# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VehicleSkillCounter.py
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleSkillCounter(DynamicScriptComponent):

    def set_counterValue(self, prev):
        if self._isAvatarReady:
            self.__updateCounter()

    def _onAvatarReady(self):
        self.__updateCounter()

    def __updateCounter(self):
        from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(events.RoleSkillEvent(events.RoleSkillEvent.COUNTER_CHANGED, {'value': self.counterValue}), scope=EVENT_BUS_SCOPE.BATTLE)