# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/maps_training/pre_queue/actions_validator.py
from CurrentVehicle import g_currentPreviewVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION
from helpers import dependency
from skeletons.gui.game_control import IMapsTrainingController

class MapsTrainingValidator(BaseActionsValidator):
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)

    def _validate(self):
        if not self.mapsTrainingController.isValid():
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE)
        if not g_currentPreviewVehicle.isPresent() or g_currentPreviewVehicle.intCD != self.mapsTrainingController.getSelectedVehicle():
            return ValidationResult(False, PREBATTLE_RESTRICTION.PREVIEW_VEHICLE_IS_PRESENT)
        return super(MapsTrainingValidator, self)._validate()


class MapsTrainingActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        baseValidator = super(MapsTrainingActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [
         baseValidator,
         MapsTrainingValidator(entity)])

    def _createVehiclesValidator(self, entity):
        return BaseActionsValidator(entity)

    def _createTutorialValidator(self, entity):
        return BaseActionsValidator(entity)