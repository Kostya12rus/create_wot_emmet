# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/minimap_component.py
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.classic.minimap import TeamsOrControlsPointsPlugin
_SCALE_FAC = 2.0 / 3.0

class EpicRandomMinimapComponent(ClassicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(EpicRandomMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup['points'] = EpicRandomTeamsOrControlsPointsPlugin
        return setup


class EpicRandomTeamsOrControlsPointsPlugin(TeamsOrControlsPointsPlugin):

    def _addPointEntry(self, symbol, position, number):
        entryID = super(EpicRandomTeamsOrControlsPointsPlugin, self)._addPointEntry(symbol, position, number)
        self._invoke(entryID, 'setScale', _SCALE_FAC)
        return entryID