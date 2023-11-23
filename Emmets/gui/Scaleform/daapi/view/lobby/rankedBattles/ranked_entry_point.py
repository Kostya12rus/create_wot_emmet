# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_entry_point.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.RankedBattlesEntryPointMeta import RankedBattlesEntryPointMeta
from gui.impl.lobby.ranked.ranked_entry_point import RankedEntryPoint

class RankedBattlesEntryPoint(RankedBattlesEntryPointMeta):

    def _makeInjectView(self):
        self.__view = RankedEntryPoint(flags=ViewFlags.VIEW)
        return self.__view