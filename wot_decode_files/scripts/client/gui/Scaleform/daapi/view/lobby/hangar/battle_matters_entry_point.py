# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/battle_matters_entry_point.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.battle_matters.battle_matters_entry_point_view import BattleMattersEntryPointView
from shared_utils import nextTick

class BattleMattersEntryPoint(InjectComponentAdaptor):

    @nextTick
    def _createInjectView(self, *args):
        super(BattleMattersEntryPoint, self)._createInjectView(*args)

    def _makeInjectView(self):
        return BattleMattersEntryPointView()