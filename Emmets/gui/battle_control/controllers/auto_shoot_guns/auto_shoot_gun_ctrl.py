# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/auto_shoot_guns/auto_shoot_gun_ctrl.py
from gui.battle_control.arena_info.interfaces import IAutoShootGunController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.auto_shoot_guns import auto_burst_controller, auto_burst_predictor

class AutoShootGunController(IAutoShootGunController):
    __slots__ = ('__burstController', '__burstPredictor')

    def __init__(self, setup):
        self.__burstPredictor = auto_burst_predictor.createBurstPredictor(setup)
        self.__burstController = auto_burst_controller.createBurstController(setup, self.__burstPredictor)

    @property
    def burstController(self):
        return self.__burstController

    @property
    def burstPredictor(self):
        return self.__burstPredictor

    def stopControl(self):
        self.__burstController.destroy()
        self.__burstPredictor.destroy()

    def getControllerID(self):
        return BATTLE_CTRL_ID.AUTOSHOOT_GUN_CTRL