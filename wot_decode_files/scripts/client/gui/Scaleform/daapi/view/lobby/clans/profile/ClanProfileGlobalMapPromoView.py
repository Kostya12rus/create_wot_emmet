# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileGlobalMapPromoView.py
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import text_styles
from gui.shared.events import OpenLinkEvent
from gui.Scaleform.daapi.view.meta.ClanProfileGlobalMapPromoViewMeta import ClanProfileGlobalMapPromoViewMeta

class ClanProfileGlobalMapPromoView(ClanProfileGlobalMapPromoViewMeta):

    def showInfo(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_PROMO))

    def showMap(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_CAP))

    def _populate(self):
        super(ClanProfileGlobalMapPromoView, self)._populate()
        self.as_setDataS({'header': text_styles.promoSubTitle(_ms(CLANS.GLOBALMAPVIEW_PROMO_HEADER)), 
           'description': text_styles.main(_ms(CLANS.GLOBALMAPVIEW_PROMO_DESCRIPTION)), 
           'infoLinkLabel': _ms(CLANS.GLOBALMAPVIEW_PROMO_INFOLINK), 
           'mapLinkLabel': _ms(CLANS.GLOBALMAPVIEW_PROMO_MAPLINK), 
           'background': RES_ICONS.MAPS_ICONS_CLANS_GLOBAL_MAP_PROMO})