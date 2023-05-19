# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/TmenXpPanel.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.meta.TmenXpPanelMeta import TmenXpPanelMeta
from CurrentVehicle import g_currentVehicle

class TmenXpPanel(TmenXpPanelMeta):

    def _populate(self):
        super(TmenXpPanel, self)._populate()
        g_currentVehicle.onChanged += self._onVehicleChange
        self._onVehicleChange()

    def _dispose(self):
        g_currentVehicle.onChanged -= self._onVehicleChange
        super(TmenXpPanel, self)._dispose()

    def _onVehicleChange(self):
        vehicle = g_currentVehicle.item
        if vehicle is None:
            self.as_setTankmenXpPanelS(False)
            LOG_DEBUG('Do not show TMenXPPanel: No current vehicle')
            return
        else:
            self.as_setTankmenXpPanelS(vehicle.isXPToTman)
            return