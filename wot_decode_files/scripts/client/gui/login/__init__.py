# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/login/__init__.py
from gui import GUI_SETTINGS
from skeletons.gui.login_manager import ILoginManager
__all__ = ('getLoginManagerConfig', )

def getLoginManagerConfig(manager):
    if GUI_SETTINGS.socialNetworkLogin['enabled']:
        from social_networks import Manager
        instance = Manager()
    else:
        from Manager import Manager
        instance = Manager()
    instance.init()
    manager.addInstance(ILoginManager, instance, finalizer='fini')