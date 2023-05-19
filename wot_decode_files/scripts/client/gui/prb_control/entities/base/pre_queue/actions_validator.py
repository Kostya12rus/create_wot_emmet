# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite, CurrentVehicleActionsValidator, TutorialActionsValidator
from gui.prb_control.items import ValidationResult

class InQueueValidator(BaseActionsValidator):

    def _validate(self):
        if self._entity.isInQueue():
            return ValidationResult(False)
        return super(InQueueValidator, self)._validate()


class PreQueueActionsValidator(ActionsValidatorComposite):

    def __init__(self, entity):
        self._stateValidator = self._createStateValidator(entity)
        self._vehiclesValidator = self._createVehiclesValidator(entity)
        self._tutorialValidator = self._createTutorialValidator(entity)
        validators = [
         self._stateValidator,
         self._vehiclesValidator,
         self._tutorialValidator]
        super(PreQueueActionsValidator, self).__init__(entity, validators)

    def _createStateValidator(self, entity):
        return InQueueValidator(entity)

    def _createVehiclesValidator(self, entity):
        return CurrentVehicleActionsValidator(entity)

    def _createTutorialValidator(self, entity):
        return TutorialActionsValidator(entity)