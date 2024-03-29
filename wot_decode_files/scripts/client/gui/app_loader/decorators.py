# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/app_loader/decorators.py
from gui.app_loader.settings import APP_NAME_SPACE as _SPACE
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
__all__ = ('app_getter', 'def_lobby', 'def_battle', 'sf_lobby', 'sf_battle')

class app_getter(property):
    appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, fget=None, doc=None, space=None):
        super(app_getter, self).__init__(fget=fget, doc=doc)
        self._space = space

    def __get__(self, obj, objType=None):
        return self.appLoader.getApp(self._space)


class def_lobby(property):
    appLoader = dependency.descriptor(IAppLoader)

    def __get__(self, obj, objType=None):
        return self.appLoader.getDefLobbyApp()


class def_battle(property):
    appLoader = dependency.descriptor(IAppLoader)

    def __get__(self, obj, objType=None):
        return self.appLoader.getDefBattleApp()


class sf_lobby(app_getter):

    def __init__(self, fget=None, doc=None):
        super(sf_lobby, self).__init__(fget, doc, _SPACE.SF_LOBBY)


class sf_battle(app_getter):

    def __init__(self, fget=None, doc=None):
        super(sf_battle, self).__init__(fget, doc, _SPACE.SF_BATTLE)