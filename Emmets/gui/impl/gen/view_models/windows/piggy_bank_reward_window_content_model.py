# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/piggy_bank_reward_window_content_model.py
from gui.impl.gen.view_models.windows.reward_window_content_model import RewardWindowContentModel

class PiggyBankRewardWindowContentModel(RewardWindowContentModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=3):
        super(PiggyBankRewardWindowContentModel, self).__init__(properties=properties, commands=commands)

    def getShowDescription(self):
        return self._getBool(3)

    def setShowDescription(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(PiggyBankRewardWindowContentModel, self)._initialize()
        self._addBoolProperty('showDescription', False)