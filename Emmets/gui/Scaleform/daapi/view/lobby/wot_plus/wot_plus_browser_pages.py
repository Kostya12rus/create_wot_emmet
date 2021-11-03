# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/wot_plus_browser_pages.py
import WWISE
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.wot_plus.sound_constants import WOT_PLUS_INFO_SOUND_SPACE, VEHICLE_RENTAL_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView

class WotPlusInfoView(WebView):
    _COMMON_SOUND_SPACE = WOT_PLUS_INFO_SOUND_SPACE

    def _populate(self):
        super(WotPlusInfoView, self)._populate()
        WWISE.WW_eventGlobal(backport.sound(R.sounds.ev_cn_wotplus_infopage_enter()))

    def _dispose(self):
        WWISE.WW_eventGlobal(backport.sound(R.sounds.ev_cn_wotplus_infopage_exit()))
        super(WotPlusInfoView, self)._dispose()


class VehicleRentalView(WebView):
    _COMMON_SOUND_SPACE = VEHICLE_RENTAL_SOUND_SPACE

    def _populate(self):
        super(VehicleRentalView, self)._populate()
        WWISE.WW_eventGlobal(backport.sound(R.sounds.ev_cn_wotplus_tank_rental_enter()))

    def _dispose(self):
        WWISE.WW_eventGlobal(backport.sound(R.sounds.ev_cn_wotplus_tank_rental_exit()))
        super(VehicleRentalView, self)._dispose()

    def webHandlers(self):
        from gui.Scaleform.daapi.view.lobby.wot_plus.web_handlers import replaceHandlers
        handlers = super(VehicleRentalView, self).webHandlers()
        replaceHandlers(handlers)
        return handlers