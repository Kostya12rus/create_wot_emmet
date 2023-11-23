# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCVehicleBuyWindow.py
from gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows import VehicleBuyWindow
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.VEHICLE_BUY_WINDOW_ALIASES import VEHICLE_BUY_WINDOW_ALIASES

class BCVehicleBuyWindow(VehicleBuyWindow):

    def _getContentLinkageFields(self):
        return {'contentLinkage': VEHICLE_BUY_WINDOW_ALIASES.CONTENT_BUY_BOOTCAMP_VIEW_UI, 
           'isContentDAAPI': True, 
           'contentAlias': VIEW_ALIAS.BOOTCAMP_VEHICLE_BUY_VIEW}