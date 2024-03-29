# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/__init__.py
from frameworks.wulf import WindowLayer
from gui import GUI_SETTINGS
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ScopeTemplates, ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.login.EULA import EULADlg
    from gui.Scaleform.daapi.view.login.IntroPage import IntroPage
    from gui.Scaleform.daapi.view.login.LegalInfoWindow import LegalInfoWindow
    from gui.Scaleform.daapi.view.login.LoginQueue import LoginQueue
    from gui.Scaleform.daapi.view.login.RssNewsFeed import RssNewsFeed
    from gui.Scaleform.daapi.view.bootcamp.bc_intro_page import BCIntroPage
    if GUI_SETTINGS.socialNetworkLogin['enabled']:
        from SocialLoginView import SocialLoginView as LoginView
    else:
        from LoginView import LoginView
    return (
     ViewSettings(VIEW_ALIAS.INTRO_VIDEO, IntroPage, 'introPage.swf', WindowLayer.VIEW, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.LOGIN, LoginView, 'login.swf', WindowLayer.VIEW, None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.EULA, EULADlg, 'EULADlg.swf', WindowLayer.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canDrag=False),
     GroupedViewSettings(VIEW_ALIAS.LEGAL_INFO_WINDOW, LegalInfoWindow, 'legalInfoWindow.swf', WindowLayer.WINDOW, 'legalInfoWindow', None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.EULA_FULL, EULADlg, 'EULAFullDlg.swf', WindowLayer.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canClose=False, canDrag=False),
     GroupedViewSettings(VIEW_ALIAS.LOGIN_QUEUE, LoginQueue, 'LoginQueueWindow.swf', WindowLayer.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE, canClose=False),
     ComponentSettings(VIEW_ALIAS.RSS_NEWS_FEED, RssNewsFeed, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.BOOTCAMP_INTRO, BCIntroPage, 'BCIntroVideo.swf', WindowLayer.TOP_WINDOW, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     LoginPackageBusinessHandler(),)


class LoginPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.EULA, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.EULA_FULL, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.INTRO_VIDEO, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LOGIN, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LEGAL_INFO_WINDOW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LOGIN_QUEUE, self.loadView),
         (
          VIEW_ALIAS.BOOTCAMP_INTRO, self.loadViewByCtxEvent))
        super(LoginPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)