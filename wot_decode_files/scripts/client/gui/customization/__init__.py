# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/customization/__init__.py
from gui.customization.service import CustomizationService
from skeletons.gui.customization import ICustomizationService
__all__ = ('getCustomizationServiceConfig', )

def getCustomizationServiceConfig(manager):

    def _create():
        instance = CustomizationService()
        instance.init()
        return instance

    manager.addRuntime(ICustomizationService, _create, finalizer='fini')