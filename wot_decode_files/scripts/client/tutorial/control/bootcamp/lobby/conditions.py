# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/bootcamp/lobby/conditions.py
from tutorial.data.conditions import CONDITION_TYPE, CONDITION_STATE, ActiveCondition

class BOOTCAMP_CONDITION_TYPE(object):
    CHECKPOINT_REACHED = CONDITION_TYPE.FIRST_CUSTOM + 0


class CheckpointReachedCondition(ActiveCondition):

    def __init__(self, entityID, state=CONDITION_STATE.ACTIVE):
        super(CheckpointReachedCondition, self).__init__(entityID, BOOTCAMP_CONDITION_TYPE.CHECKPOINT_REACHED, state)