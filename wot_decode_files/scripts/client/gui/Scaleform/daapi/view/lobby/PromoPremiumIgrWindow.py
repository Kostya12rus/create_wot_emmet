# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/PromoPremiumIgrWindow.py
from account_helpers.AccountSettings import AccountSettings, IGR_PROMO
from gui.Scaleform.daapi.view.meta.PromoPremiumIgrWindowMeta import PromoPremiumIgrWindowMeta
from gui.shared.formatters import icons, text_styles
from helpers import i18n
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS

class PromoPremiumIgrWindow(PromoPremiumIgrWindowMeta):

    def __init__(self, _=None):
        super(PromoPremiumIgrWindow, self).__init__()

    def _populate(self):
        super(PromoPremiumIgrWindow, self)._populate()
        self.__initData()

    def onWindowClose(self):
        self.destroy()

    def _dispose(self):
        AccountSettings.setFilter(IGR_PROMO, {'wasShown': True})
        super(PromoPremiumIgrWindow, self)._dispose()

    def __initData(self):
        ms = i18n.makeString
        igrIcon = RES_ICONS.MAPS_ICONS_LIBRARY_PREMIUM_SMALL
        icon = icons.makeImageTag(igrIcon, 34, 16, -4)
        self.as_setWindowTitleS(ms(MENU.PROMOPREMIUMIGRWINDOW_WINDOWTITLE))
        self.as_setTitleS(text_styles.highTitle(ms(MENU.PROMOPREMIUMIGRWINDOW_TITLE)))
        self.as_setTextS(text_styles.standard(ms(MENU.PROMOPREMIUMIGRWINDOW_TEXT, iconIgr=icon)))
        self.as_setApplyButtonLabelS(ms(MENU.PROMOPREMIUMIGRWINDOW_APPLYBUTTONLABEL))