# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/MiniclientDescriptionWindow.py
from gui import GUI_SETTINGS
from gui.shared import g_eventBus, events
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IBrowserController, IBootcampController

class MiniclientDescriptionWindow(object):
    browserCtrl = dependency.descriptor(IBrowserController)
    bootcampCtrl = dependency.descriptor(IBootcampController)

    def __init__(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__openDescriptionInBrowser)

    def __openDescriptionInBrowser(self, event):
        if not self.bootcampCtrl.isInBootcamp():
            self.browserCtrl.load(url=('{0}/$LANGUAGE_CODE/greeting/mini_wot/').format(GUI_SETTINGS.baseUrls['webBridgeRootURL']), title=_ms('#miniclient:hangar/miniclient_description_window/title'), browserSize=(780,
                                                                                                                                                                                                                     450), showCloseBtn=True, showActionBtn=False, isAsync=True, showWaiting=False)((lambda success: True))
            g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__openDescriptionInBrowser)