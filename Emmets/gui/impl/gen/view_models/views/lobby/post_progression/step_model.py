# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/step_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.post_progression.base_step_model import BaseStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.restrictions_model import RestrictionsModel

class ActionState(Enum):
    PERSISTENT = 'persistent'
    SELECTABLE = 'selectable'
    CHANGEABLE = 'changeable'


class StepState(Enum):
    RESTRICTED = 'restricted'
    UNAVAILABLELOCKED = 'unavailableLocked'
    AVAILABLEPURCHASE = 'availablePurchase'
    RECEIVED = 'received'


class StepModel(BaseStepModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(StepModel, self).__init__(properties=properties, commands=commands)

    @property
    def restrictions(self):
        return self._getViewModel(2)

    @staticmethod
    def getRestrictionsType():
        return RestrictionsModel

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)

    def getActionState(self):
        return ActionState(self._getString(4))

    def setActionState(self, value):
        self._setString(4, value.value)

    def getStepState(self):
        return StepState(self._getString(5))

    def setStepState(self, value):
        self._setString(5, value.value)

    def _initialize(self):
        super(StepModel, self)._initialize()
        self._addViewModelProperty('restrictions', RestrictionsModel())
        self._addBoolProperty('isDisabled', False)
        self._addStringProperty('actionState')
        self._addStringProperty('stepState')