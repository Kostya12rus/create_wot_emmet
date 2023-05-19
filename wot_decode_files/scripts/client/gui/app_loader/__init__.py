# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/app_loader/__init__.py
from gui.app_loader import settings
from gui.app_loader.decorators import app_getter
from gui.app_loader.decorators import def_lobby
from gui.app_loader.decorators import def_battle
from gui.app_loader.decorators import sf_lobby
from gui.app_loader.decorators import sf_battle
__all__ = ('getAppLoaderConfig', 'decorators', 'settings', 'app_getter', 'def_lobby',
           'def_battle', 'sf_lobby', 'sf_battle')

def getAppLoaderConfig(manager):
    from gui.app_loader.loader import AppLoader
    from skeletons.gui.app_loader import IAppLoader
    manager.addInstance(IAppLoader, AppLoader(), finalizer='fini')