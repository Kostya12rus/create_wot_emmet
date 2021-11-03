# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/battle_royale/markers2d/manager.py
from gui.Scaleform.daapi.view.battle.battle_royale.markers2d import plugins
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import MarkersManager

class BattleRoyaleMarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(BattleRoyaleMarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = plugins.BattleRoyaleVehicleMarkerPlugin
        setup['settings'] = plugins.BattleRoyaleSettingsPlugin
        return setup