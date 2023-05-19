# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/markers2d/manager.py
from gui.Scaleform.daapi.view.battle.comp7.markers2d import plugins
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import MarkersManager
from gui.Scaleform.daapi.view.battle.shared.points_of_interest import markers2d as poi_plugins

class Comp7MarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(Comp7MarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = plugins.Comp7VehicleMarkerPlugin
        setup['settings'] = plugins.Comp7SettingsPlugin
        setup['pointsOfInterest'] = poi_plugins.PointsOfInterestPlugin
        return setup