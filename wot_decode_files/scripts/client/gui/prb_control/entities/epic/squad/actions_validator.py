# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/epic/squad/actions_validator.py
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator
from gui.prb_control.entities.random.squad.actions_validator import BalancedSquadVehiclesValidator, SPGForbiddenSquadVehiclesValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator
from helpers import time_utils, dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator

class _EpicVehiclesValidator(SquadVehiclesValidator):

    def _isValidMode(self, vehicle):
        return not vehicle.isEvent


class _EpicBalancedSquadVehiclesValidator(BalancedSquadVehiclesValidator):
    __epicCtrl = dependency.descriptor(IEpicBattleMetaGameController)

    def _validate(self):
        availableLevels = self.__epicCtrl.getSuitableForQueueVehicleLevels()
        pInfo = self._entity.getPlayerInfo()
        if not pInfo.isReady and g_currentVehicle.isPresent() and g_currentVehicle.item.level not in availableLevels:
            return ValidationResult(False, UNIT_RESTRICTION.VEHICLE_INVALID_LEVEL)
        return super(_EpicBalancedSquadVehiclesValidator, self)._validate()


class _EpicStateValidator(UnitStateValidator):
    __epicCtrl = dependency.descriptor(IEpicBattleMetaGameController)

    def _validate(self):
        currentSeason = self.__epicCtrl.getCurrentSeason()
        if currentSeason:
            if currentSeason.hasActiveCycle(time_utils.getCurrentLocalServerTimestamp()):
                return super(_EpicStateValidator, self)._validate()
        return ValidationResult(False, UNIT_RESTRICTION.UNIT_INACTIVE_PERIPHERY_UNDEF)


class EpicSquadActionsValidator(SquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        return ActionsValidatorComposite(entity, validators=[
         _EpicBalancedSquadVehiclesValidator(entity),
         _EpicVehiclesValidator(entity),
         SPGForbiddenSquadVehiclesValidator(entity)])

    def _createStateValidator(self, entity):
        return _EpicStateValidator(entity)

    def _createSlotsValidator(self, entity):
        baseValidator = super(EpicSquadActionsValidator, self)._createSlotsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         baseValidator,
         EpicSquadSlotsValidator(entity)])


class EpicSquadSlotsValidator(CommanderValidator):

    def _validate(self):
        stats = self._entity.getStats()
        pInfo = self._entity.getPlayerInfo()
        if stats.occupiedSlotsCount > 1 and not pInfo.isReady:
            return ValidationResult(False, UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED)