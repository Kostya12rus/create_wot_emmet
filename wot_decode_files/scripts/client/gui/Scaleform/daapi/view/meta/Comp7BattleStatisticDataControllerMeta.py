# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/Comp7BattleStatisticDataControllerMeta.py
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController

class Comp7BattleStatisticDataControllerMeta(ClassicStatisticsDataController):

    def as_removePointOfInterestS(self, vehicleID, type):
        if self._isDAAPIInited():
            return self.flashObject.as_removePointOfInterest(vehicleID, type)

    def as_updatePointOfInterestS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePointOfInterest(data)