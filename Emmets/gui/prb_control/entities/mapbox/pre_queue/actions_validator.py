# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/mapbox/pre_queue/actions_validator.py
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite, CurrentVehicleActionsValidator
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import IMapboxController

class MapboxVehicleValidator(CurrentVehicleActionsValidator):

    def _validate(self):
        vehicle = g_currentVehicle.item
        result = self.validateForMapbox(vehicle)
        if result is not None:
            return result
        else:
            return super(MapboxVehicleValidator, self)._validate()

    @staticmethod
    def validateForMapbox(vehicle):
        if vehicle is None:
            return ValidationResult(False, PREBATTLE_RESTRICTION.VEHICLE_NOT_PRESENT)
        else:
            lobbyContext = dependency.instance(ILobbyContext)
            config = lobbyContext.getServerSettings().mapbox
            if vehicle.level not in config.levels:
                return ValidationResult(False, PRE_QUEUE_RESTRICTION.LIMIT_LEVEL, {'levels': config.levels})
            if vehicle.intCD in config.forbiddenVehTypes:
                return ValidationResult(False, PRE_QUEUE_RESTRICTION.LIMIT_VEHICLE_TYPE, {'forbiddenType': vehicle.shortUserName})
            if vehicle.type in config.forbiddenClassTags:
                return ValidationResult(False, PRE_QUEUE_RESTRICTION.LIMIT_VEHICLE_CLASS, {'forbiddenClass': vehicle.type})
            return


class MapboxStateValidator(BaseActionsValidator):

    def _validate(self):
        mapboxController = dependency.instance(IMapboxController)
        if not mapboxController.isActive() or not mapboxController.isInPrimeTime():
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE)
        return super(MapboxStateValidator, self)._validate()


class MapboxActionsValidator(PreQueueActionsValidator):

    def _createVehiclesValidator(self, entity):
        baseValidator = super(MapboxActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, [
         MapboxVehicleValidator(entity),
         baseValidator])

    def _createStateValidator(self, entity):
        baseValidator = super(MapboxActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [
         baseValidator,
         MapboxStateValidator(entity)])