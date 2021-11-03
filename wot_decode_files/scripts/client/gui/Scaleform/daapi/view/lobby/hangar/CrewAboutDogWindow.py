# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/CrewAboutDogWindow.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS

class CrewAboutDogWindow(SimpleWindowMeta):

    def __init__(self, ctx=None):
        super(CrewAboutDogWindow, self).__init__()

    def onBtnClick(self, action):
        if action == 'closeAction':
            self.destroy()

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(CrewAboutDogWindow, self)._populate()
        self.__populateData()

    def __populateData(self):
        self.as_setImageS(RES_ICONS.MAPS_ICONS_TANKMEN_WINDOWS_ABOUTRUDY, -70)
        self.as_setWindowTitleS(MENU.HANGAR_CREW_RODY_DOG_WINDOW_TITLE)
        self.as_setTextS(MENU.HANGAR_CREW_RODY_DOG_WINDOW_HEADER, MENU.HANGAR_CREW_RODY_DOG_WINDOW_DESCRIPTION)
        self.as_setButtonsS(self.getBtnData(), 'right', 120)

    def getBtnData(self):
        return [
         {'label': MENU.HANGAR_CREW_RODY_DOG_WINDOW_CLOSEBTNLABEL, 
            'btnLinkage': 'ButtonBlack', 
            'action': 'closeAction', 
            'isFocused': True, 
            'tooltip': ''}]