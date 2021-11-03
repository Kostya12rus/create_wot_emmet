# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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
        return

    def setController(self, controller):
        controller.activate()
        self._controller = weakref.ref(controller)

    def removeController(self):
        self._controller = lambda : None

    def setActive(self, active):
        self.as_clickEnabled(active)

    def setClick(self, x, y):
        controller = self._controller()
        if controller:
            command = controller.proto.unitChat.createByMapPos(x, y)
            controller.sendCommand(command)

    def addCommand(self, cmd):
        if cmd.isOnMinimap():
            self.as_addPointS(cmd.getMapPosX(), cmd.getMapPosY())

    def as_addMessageS(self, message):
        pass

    def as_setJoinedS(self, flag):
        pass