# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/__init__.py
import typing
from gui.platform.wgnp.steam_account.controller import WGNPSteamAccRequestController
from gui.platform.wgnp.demo_account.controller import WGNPDemoAccRequestController
from gui.platform.wgnp.general.controller import WGNPGeneralRequestController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController, IWGNPDemoAccRequestController, IWGNPGeneralRequestController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getWGNPRequestControllers', )

def getWGNPRequestControllers(manager):
    wgnpSteamAccController = WGNPSteamAccRequestController()
    wgnpSteamAccController.init()
    manager.addInstance(IWGNPSteamAccRequestController, wgnpSteamAccController, finalizer='fini')
    wgnpDemoAccController = WGNPDemoAccRequestController()
    wgnpDemoAccController.init()
    manager.addInstance(IWGNPDemoAccRequestController, wgnpDemoAccController, finalizer='fini')
    wgnpGeneralController = WGNPGeneralRequestController()
    wgnpGeneralController.init()
    manager.addInstance(IWGNPGeneralRequestController, wgnpGeneralController, finalizer='fini')