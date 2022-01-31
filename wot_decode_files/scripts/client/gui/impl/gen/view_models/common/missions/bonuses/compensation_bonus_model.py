# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/bonuses/compensation_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class CompensationBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(CompensationBonusModel, self).__init__(properties=properties, commands=commands)

    @property
    def compensatedItem(self):
        return self._getViewModel(7)

    def _initialize(self):
        super(CompensationBonusModel, self)._initialize()
        self._addViewModelProperty('compensatedItem', BonusModel())