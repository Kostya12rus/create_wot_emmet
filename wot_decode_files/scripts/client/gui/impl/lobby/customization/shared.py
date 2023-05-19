# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/customization/shared.py
from CurrentVehicle import g_currentVehicle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.customization.constants import CustomizationModes
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.customization import ICustomizationService

def goToC11nStyledMode():
    c11nService = dependency.instance(ICustomizationService)
    appLoader = dependency.instance(IAppLoader)
    app = appLoader.getApp()
    app.containerManager.destroyViews(VIEW_ALIAS.BATTLE_RESULTS)

    def styleCallback():
        ctx = c11nService.getCtx()
        ctx.changeMode(CustomizationModes.STYLED)

    c11nService.showCustomization(g_currentVehicle.item.invID, callback=styleCallback)