# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/tech_tree/pointcuts.py
import aspects
from helpers import aop

class OnTechTreePopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.techtree.techtree_page', 'TechTree', '_populate', aspects=(
         aspects.OnTechTreePopulate,))


class OnBuyVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows', 'VehicleBuyWindow', 'submit', aspects=(
         aspects.OnBuyVehicle(config),))


class OnRestoreVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows', 'VehicleRestoreWindow', 'submit', aspects=(
         aspects.OnRestoreVehicle(config),))