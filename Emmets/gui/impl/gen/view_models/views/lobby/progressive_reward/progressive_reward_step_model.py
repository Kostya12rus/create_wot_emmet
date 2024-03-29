# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/progressive_reward/progressive_reward_step_model.py
from frameworks.wulf import ViewModel

class ProgressiveRewardStepModel(ViewModel):
    __slots__ = ()
    PR_STATE_NOT_RECEIVED = 'not_received'
    PR_STATE_OPENED = 'opened'
    PR_STATE_PROB_MIN = 'prob_min'
    PR_STATE_PROB_MED = 'prob_med'
    PR_STATE_PROB_MAX = 'prob_max'
    PR_STATE_RECEIVED = 'received'
    PR_TYPE_SMALL = 'small'
    PR_TYPE_BIG = 'big'
    PR_TYPE_SMALL_HIDDEN = 'small_hidden'
    PR_TYPE_BIG_HIDDEN = 'big_hidden'

    def __init__(self, properties=3, commands=0):
        super(ProgressiveRewardStepModel, self).__init__(properties=properties, commands=commands)

    def getStepState(self):
        return self._getString(0)

    def setStepState(self, value):
        self._setString(0, value)

    def getRewardType(self):
        return self._getString(1)

    def setRewardType(self, value):
        self._setString(1, value)

    def getHasPreviousStep(self):
        return self._getBool(2)

    def setHasPreviousStep(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(ProgressiveRewardStepModel, self)._initialize()
        self._addStringProperty('stepState', 'not_received')
        self._addStringProperty('rewardType', 'small')
        self._addBoolProperty('hasPreviousStep', True)