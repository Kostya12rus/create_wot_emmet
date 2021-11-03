# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/manager.py
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
from gui.Scaleform.daapi.view.battle.event.plugins import EventVehicleMarkerPlugin, EventCampsOrControlsPointsPlugin, EventEquipmentsMarkerPlugin
from account_helpers.settings_core.settings_constants import BattleCommStorageKeys

class EventMarkersManager(MarkersManager):

    def _populate(self):
        self.settingsCore.applySetting(BattleCommStorageKeys.SHOW_STICKY_MARKERS, True)
        self.settingsCore.applySetting(BattleCommStorageKeys.SHOW_BASE_MARKERS, True)
        self.settingsCore.confirmChanges(self.settingsCore.applyStorages(restartApproved=False))
        self.settingsCore.clearStorages()
        super(EventMarkersManager, self)._populate()

    def _setupPlugins(self, arenaVisitor):
        setup = super(EventMarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = EventVehicleMarkerPlugin
        setup['teamAndControlPoints'] = EventCampsOrControlsPointsPlugin
        setup['equipments'] = EventEquipmentsMarkerPlugin
        return setup