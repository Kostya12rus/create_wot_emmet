# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/bp_exchange_vehicle_preview.py
from gui.Scaleform.daapi.view.lobby.vehicle_preview.style_preview import VehicleStylePreview

class BlueprintsExchangeVehicleStypePreview(VehicleStylePreview):

    def onBackClick(self):
        self.closeView()
        super(BlueprintsExchangeVehicleStypePreview, self).onBackClick()