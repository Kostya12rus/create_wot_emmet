# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/SquadPromoWindow.py
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.daapi.view.meta.SquadPromoWindowMeta import SquadPromoWindowMeta
from gui.Scaleform.genConsts.TEXT_ALIGN import TEXT_ALIGN

class SquadPromoWindow(SquadPromoWindowMeta):
    _BTN_WIDTH = 120
    _CLOSE_BTN_ACTION = 'closeAction'

    def __init__(self, ctx=None):
        super(SquadPromoWindow, self).__init__()

    def onBtnClick(self, action):
        if action == self._CLOSE_BTN_ACTION:
            self.onWindowClose()

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(SquadPromoWindow, self)._populate()
        self.as_setImageS(RES_ICONS.MAPS_ICONS_WINDOWS_MINICLIENT_SQUAD_WINDOW_BACKGROUND, 0)
        self.as_setWindowTitleS(_ms('#menu:headerButtons/btnLabel/inSquad'))
        self.as_setTextS(_ms('#miniclient:squad_promo_window/header'), _ms('#miniclient:squad_promo_window/description'))
        self.as_setHyperlinkS(_ms('#miniclient:personal_quests_welcome_view/continue_download'))
        self.as_setButtonsS([
         {'label': _ms('#miniclient:squad_promo_window/btn'), 
            'btnLinkage': BUTTON_LINKAGES.BUTTON_NORMAL, 
            'action': self._CLOSE_BTN_ACTION, 
            'isFocused': True, 
            'tooltip': ''}], TEXT_ALIGN.RIGHT, self._BTN_WIDTH)