# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/RespawnDeathMode.py
import weakref, BigWorld, GUI, SoundGroups, BattleReplay
from AvatarInputHandler import aih_global_binding
from DynamicCameras.ArcadeCamera import ArcadeCamera
from control_modes import IControlMode
from math_utils import clamp
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class RespawnDeathMode(IControlMode):
    camera = property((lambda self: self.__cam))
    isEnabled = property((lambda self: self.__isEnabled))
    curVehicleID = property((lambda self: self.__curVehicleID))
    aimingMode = property((lambda self: self._aimingMode))
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    __aimOffset = aih_global_binding.bindRO(aih_global_binding.BINDING_ID.AIM_OFFSET)

    def __init__(self, dataSection, avatarInputHandler):
        self.__aih = weakref.proxy(avatarInputHandler)
        self.__cam = ArcadeCamera(dataSection['camera'], dataSection.readVector2('defaultOffset'))
        self.__isEnabled = False
        self.__curVehicleID = None
        self._aimingMode = 0
        return

    def create(self):
        self.__cam.create(None, True)
        return

    def destroy(self):
        self.disable()
        self.__cam.destroy()
        self.__cam = None
        return

    def enable(self, **args):
        BattleReplay.g_replayCtrl.onRespawnMode(True)
        SoundGroups.g_instance.changePlayMode(0)
        self.__cam.enable(None, False, args.get('postmortemParams'))
        self.__cam.reinitMatrix()
        player = BigWorld.player()
        self.__curVehicleID = player.playerVehicleID
        ctrl = self.guiSessionProvider.dynamic.respawn
        if hasattr(ctrl, 'showUiAllowed'):
            ctrl.showUiAllowed = True
        self.__isEnabled = True
        return

    def disable(self):
        self.__isEnabled = False
        self.__cam.disable()
        ctrl = self.guiSessionProvider.dynamic.respawn
        if hasattr(ctrl, 'showUiAllowed'):
            ctrl.showUiAllowed = False
        BattleReplay.g_replayCtrl.onRespawnMode(False)

    def handleMouseEvent(self, dx, dy, dz):
        GUI.mcursor().position = self.__aimOffset
        self.__cam.update(dx, dy, clamp(-1.0, 1.0, dz))
        return True