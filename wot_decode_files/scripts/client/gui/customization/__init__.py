# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/customization/__init__.py
from skeletons.gui.customization import ICustomizationService
__all__ = ('getCustomizationServiceConfig', )

def getCustomizationServiceConfig(manager):
    from gui.customization.service import CustomizationService

    def _create():
        instance = CustomizationService()
        instance.init()
        return instance

    manager.addRuntime(ICustomizationService, _create, finalizer='fini')