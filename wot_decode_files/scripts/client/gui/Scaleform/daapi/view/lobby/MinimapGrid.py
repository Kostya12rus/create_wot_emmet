# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/MinimapGrid.py
import weakref
from gui.Scaleform.daapi.view.meta.MinimapGridMeta import MinimapGridMeta
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

class MinimapGrid(MinimapGridMeta):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(MinimapGrid, self).__init__()
        self._channel = None
        self._controller = None
        self.__mapId = 0
        return

    def setController(self, controller):
        controller.activate()
        self._controller = weakref.ref(controller)

    def removeController(self):
        self._controller = lambda : None

    def setActive(self, active):
        self.as_clickEnabledS(active)

    def setClick(self, x, y):
        controller = self._controller()
        if controller:
            command = controller.proto.unitChat.createByMapPos(x, y)
            controller.sendCommand(command)

    def setMapId(self, mapId):
        if mapId != self.__mapId:
            self.as_clearPointsS()
        self.__mapId = mapId

    def addCommand(self, cmd):
        if cmd.isOnMinimap():
            self.as_addPointS(cmd.getMapPosX(), cmd.getMapPosY())

    def as_addMessageS(self, message):
        pass

    def as_setJoinedS(self, flag):
        pass