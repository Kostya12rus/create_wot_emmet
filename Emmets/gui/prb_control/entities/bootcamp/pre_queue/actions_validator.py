# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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