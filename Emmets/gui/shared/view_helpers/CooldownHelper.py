# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/view_helpers/CooldownHelper.py
import operator, BigWorld
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.rq_cooldown import getRequestCoolDown

class CooldownHelper(object):

    def __init__(self, requestIDs, handler, eventType, eventScope=EVENT_BUS_SCOPE.LOBBY):
        self._eventType = eventType
        self._eventScope = eventScope
        self._requestIDs = requestIDs
        self._cooldownCbID = None
        self.__handler = handler
        self.__isInCooldown = False
        return

    def start(self):
        g_eventBus.addListener(self._eventType, self._handleSetCoolDown, scope=self._eventScope)
        self._checkCooldowns()

    def stop(self):
        self._cancelCallback()
        g_eventBus.removeListener(self._eventType, self._handleSetCoolDown, scope=self._eventScope)

    def isInCooldown(self):
        return self.__isInCooldown

    def _handleSetCoolDown(self, event):
        if event.requestID in self._requestIDs and event.coolDown > 0:
            self.__isInCooldown = True
            self.__handler(True)
            self._loadCallback(event.coolDown)

    def _loadCallback(self, cooldown):
        self._cancelCallback()
        self._cooldownCbID = BigWorld.callback(cooldown, self._onCooldownTimeLeft)

    def _cancelCallback(self):
        if self._cooldownCbID is not None:
            BigWorld.cancelCallback(self._cooldownCbID)
            self._cooldownCbID = None
        return

    def _onCooldownTimeLeft(self):
        self._cancelCallback()
        self.__isInCooldown = False
        self.__handler(False)

    def _checkCooldowns(self):
        cooldowns = {}
        for requestID in self._requestIDs:
            cooldowns[requestID] = getRequestCoolDown(self._eventScope, requestID)

        if cooldowns:
            requestID, cooldown = max(cooldowns.items(), key=operator.itemgetter(1))
            if cooldown > 0:
                self.__isInCooldown = True
                self.__handler(True)
                self._loadCallback(cooldown)