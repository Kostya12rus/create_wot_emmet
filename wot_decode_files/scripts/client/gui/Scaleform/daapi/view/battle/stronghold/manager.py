# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/stronghold/manager.py
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
from gui.Scaleform.daapi.view.battle.stronghold.plugins import StrongholdVehicleMarkerPlugin

class StrongholdMarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(StrongholdMarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = StrongholdVehicleMarkerPlugin
        return setup