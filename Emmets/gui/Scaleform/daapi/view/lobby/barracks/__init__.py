# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/barracks/__init__.py
from frameworks.wulf import WindowLayer
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.barracks.Barracks import Barracks
    return (
     ViewSettings(VIEW_ALIAS.LOBBY_BARRACKS, Barracks, 'barracks.swf', WindowLayer.SUB_VIEW, VIEW_ALIAS.LOBBY_BARRACKS, ScopeTemplates.LOBBY_SUB_SCOPE),)


def getBusinessHandlers():
    return (
     BarracksPackageBusinessHandler(),)


class BarracksPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.LOBBY_BARRACKS, self.loadViewByCtxEvent),)
        super(BarracksPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)