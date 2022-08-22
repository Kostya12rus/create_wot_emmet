# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/telecom_rentals/telecom_rentals_browser_pages.py
from gui.Scaleform.daapi.view.lobby import VehicleRentalView
from gui.Scaleform.daapi.view.lobby.wot_plus.sound_constants import VEHICLE_RENTAL_SOUND_SPACE

class VehicleTelecomRentalView(VehicleRentalView):
    _COMMON_SOUND_SPACE = VEHICLE_RENTAL_SOUND_SPACE

    def webHandlers(self):
        from gui.Scaleform.daapi.view.lobby.telecom_rentals.web_handlers import replaceHandlers
        handlers = super(VehicleTelecomRentalView, self).webHandlers()
        replaceHandlers(handlers)
        return handlers