# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/epic_battle_training/actions_validator.py
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite, BaseActionsValidator
from gui.prb_control.entities.base.legacy.actions_validator import LegacyVehicleValid
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.items import ValidationResult

class TrainingIsLoaded(BaseActionsValidator):

    def _validate(self):
        if g_eventDispatcher.isEpicTrainingLoaded():
            return ValidationResult(False)
        return super(TrainingIsLoaded, self)._validate()


class TrainingIntroActionsValidator(ActionsValidatorComposite):

    def __init__(self, entity):
        validators = [
         TrainingIsLoaded(entity)]
        super(TrainingIntroActionsValidator, self).__init__(entity, validators)


class TrainingActionsValidator(TrainingIntroActionsValidator):

    def __init__(self, entity):
        super(TrainingActionsValidator, self).__init__(entity)
        self.addValidator(LegacyVehicleValid(entity))