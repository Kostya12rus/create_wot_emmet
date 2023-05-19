# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/marathon/bonuses_event_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.marathon.base_event_model import BaseEventModel

class BonusesEventModel(BaseEventModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=1):
        super(BonusesEventModel, self).__init__(properties=properties, commands=commands)

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(BonusesEventModel, self)._initialize()
        self._addArrayProperty('bonuses', Array())