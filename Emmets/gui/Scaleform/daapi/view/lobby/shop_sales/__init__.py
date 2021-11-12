# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/shop_sales/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.shop_sales.main_view import ShopSalesMainView
    from gui.Scaleform.framework import ViewSettings, ScopeTemplates
    return (
     ViewSettings(VIEW_ALIAS.SHOP_SALES_MAIN_VIEW, ShopSalesMainView, 'browserScreen.swf', WindowLayer.FULLSCREEN_WINDOW, VIEW_ALIAS.SHOP_SALES_MAIN_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE),)


def getBusinessHandlers():
    return (
     ShopSalesPackageBusinessHandler(),)


class ShopSalesPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.SHOP_SALES_MAIN_VIEW, self.loadViewByCtxEvent),)
        super(ShopSalesPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)