# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/Comp7BattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class Comp7BattlePageMeta(ClassicPage):

    def showHelp(self):
        self._printOverrideError('showHelp')

    def moveSpace(self, x, y, delta):
        self._printOverrideError('moveSpace')

    def notifyCursorOver3dScene(self, isOver3dScene):
        self._printOverrideError('notifyCursorOver3dScene')

    def notifyCursorDragging(self, isDragging):
        self._printOverrideError('notifyCursorDragging')

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)

    def as_onVehicleSelectionConfirmedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onVehicleSelectionConfirmed()

    def as_onBattleStartedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onBattleStarted()

    def as_onPrebattleInputStateLockedS(self, isStateLocked):
        if self._isDAAPIInited():
            return self.flashObject.as_onPrebattleInputStateLocked(isStateLocked)