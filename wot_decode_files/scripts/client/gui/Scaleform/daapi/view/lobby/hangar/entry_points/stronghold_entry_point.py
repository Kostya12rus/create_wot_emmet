# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/entry_points/stronghold_entry_point.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.StrongholdEntryPointMeta import StrongholdEntryPointMeta
from gui.impl.lobby.stronghold.stronghold_entry_point_view import StrongholdEntryPointView

class StrongholdEntryPoint(StrongholdEntryPointMeta):

    def _makeInjectView(self):
        self.__view = StrongholdEntryPointView(ViewFlags.COMPONENT)
        return self.__view

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)