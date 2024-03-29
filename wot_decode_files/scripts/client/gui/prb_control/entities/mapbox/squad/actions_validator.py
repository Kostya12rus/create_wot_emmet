# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/mapbox/squad/actions_validator.py
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator
from gui.prb_control.entities.random.squad.actions_validator import BalancedSquadVehiclesValidator, SPGForbiddenSquadVehiclesValidator, ScoutForbiddenSquadVehiclesValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator
from helpers import dependency
from skeletons.gui.game_control import IMapboxController
from gui.periodic_battles.models import PrimeTimeStatus

class _MapboxVehicleValidator(SquadVehiclesValidator):

    def _isValidMode(self, vehicle):
        return not vehicle.isEvent


class _MapboxStateValidator(UnitStateValidator):

    def _validate(self):
        mapboxCtrl = dependency.instance(IMapboxController)
        status, _, _ = mapboxCtrl.getPrimeTimeStatus()
        if status != PrimeTimeStatus.AVAILABLE:
            return ValidationResult(False, UNIT_RESTRICTION.CURFEW)
        return super(_MapboxStateValidator, self)._validate()


class _UnitSlotsValidator(CommanderValidator):

    def _validate(self):
        stats = self._entity.getStats()
        pInfo = self._entity.getPlayerInfo()
        if stats.occupiedSlotsCount > 1 and not pInfo.isReady:
            return ValidationResult(False, UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED)


class MapboxSquadActionsValidator(SquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        return ActionsValidatorComposite(entity, validators=[
         BalancedSquadVehiclesValidator(entity),
         _MapboxVehicleValidator(entity),
         SPGForbiddenSquadVehiclesValidator(entity),
         ScoutForbiddenSquadVehiclesValidator(entity)])

    def _createStateValidator(self, entity):
        return _MapboxStateValidator(entity)

    def _createSlotsValidator(self, entity):
        baseValidator = super(MapboxSquadActionsValidator, self)._createSlotsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         baseValidator,
         _UnitSlotsValidator(entity)])