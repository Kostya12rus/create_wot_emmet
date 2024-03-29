# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/hangar/pointcuts.py
import aspects
from helpers import aop

class ShowMiniclientInfo(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.Hangar', 'Hangar', '_populate', aspects=(
         aspects.ShowMiniclientInfo,))


class DisableTankServiceButtons(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.Hangar', 'Hangar', 'as_setupAmmunitionPanelS', aspects=(
         aspects.DisableTankServiceButtons(config),))


class TankModelHangarVisibility(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'CurrentVehicle', '_CurrentVehicle', 'isInHangar', aspects=(
         aspects.TankModelHangarVisibility(config),))


class TankHangarStatus(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'CurrentVehicle', '_CurrentVehicle', 'getHangarMessage', aspects=(
         aspects.TankHangarStatus(config),))


class EnableCrew(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.Hangar', 'Hangar', 'as_setCrewEnabledS', aspects=(
         aspects.EnableCrew(config),))


class ChangeLobbyMenuTooltip(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby', 'LobbyMenu', '_getVersionMessage', aspects=(
         aspects.ChangeLobbyMenuTooltip,))