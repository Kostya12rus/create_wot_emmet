# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCVehicleBuyWindow.py
from gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows import VehicleBuyWindow
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.VEHICLE_BUY_WINDOW_ALIASES import VEHICLE_BUY_WINDOW_ALIASES

class BCVehicleBuyWindow(VehicleBuyWindow):

    def _getContentLinkageFields(self):
        return {'contentLinkage': VEHICLE_BUY_WINDOW_ALIASES.CONTENT_BUY_BOOTCAMP_VIEW_UI, 
           'isContentDAAPI': True, 
           'contentAlias': VIEW_ALIAS.BOOTCAMP_VEHICLE_BUY_VIEW}