# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/bootcamp/pre_queue/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from helpers import dependency
from skeletons.gui.game_control import IDemoAccCompletionController

class BootcampStateValidator(BaseActionsValidator):

    def _validate(self):
        demoAccController = dependency.instance(IDemoAccCompletionController)
        if demoAccController.isInDemoAccRegistration:
            return ValidationResult(False)
        return super(BootcampStateValidator, self)._validate()


class BootcampActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        baseValidator = super(BootcampActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [
         baseValidator,
         BootcampStateValidator(entity)])