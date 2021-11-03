# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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