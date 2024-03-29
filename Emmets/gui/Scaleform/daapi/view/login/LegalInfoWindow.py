# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/LegalInfoWindow.py
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.view.meta.LegalInfoWindowMeta import LegalInfoWindowMeta
from debug_utils import LOG_ERROR
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE
from gui.shared import events

class LegalInfoWindow(LegalInfoWindowMeta):

    def __init__(self, ctx=None):
        super(LegalInfoWindow, self).__init__()

    def startListening(self):
        self.addListener(events.HideWindowEvent.HIDE_LEGAL_INFO_WINDOW, self.__handleLIWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)

    def stopListening(self):
        self.removeListener(events.HideWindowEvent.HIDE_LEGAL_INFO_WINDOW, self.__handleLIWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)

    def __handleLIWindowHide(self, _):
        self.destroy()

    def _populate(self):
        self.startListening()
        super(LegalInfoWindow, self)._populate()

    def _dispose(self):
        self.stopListening()
        super(LegalInfoWindow, self)._dispose()

    def getLegalInfo(self):
        info = ''
        LICENSES_PATH = 'licenses.txt'
        try:
            f = open(LICENSES_PATH, 'r')
        except IOError:
            LOG_ERROR('cannot open %s' % LICENSES_PATH)
        else:
            info = f.read()
            info = info.format(header_1=backport.text(R.strings.menu.login.licenses.header_1()), header_2=backport.text(R.strings.menu.login.licenses.header_2()), vivoxLicense=GUI_SETTINGS.vivoxLicense.replace('\\n', '\n'))
            f.close()

        self.as_setLegalInfoS(info)

    def onCancelClick(self):
        self.destroy()

    def onWindowClose(self):
        self.destroy()