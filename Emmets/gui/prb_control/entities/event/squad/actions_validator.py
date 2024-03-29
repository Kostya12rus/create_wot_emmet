# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/actions_validator.py
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION

class _EventBattleVehiclesValidator(SquadVehiclesValidator):

    def _validate(self):
        leaderEventEnqueueData = self._entity.getLeaderEventEnqueueData()
        if leaderEventEnqueueData is not None:
            result = True
            if not result:
                return ValidationResult(False, UNIT_RESTRICTION.UNIT_WRONG_DATA)
        return super(_EventBattleVehiclesValidator, self)._validate()

    def _isValidMode(self, vehicle):
        return vehicle.isEvent and not vehicle.isOnlyForEpicBattles


class EventSquadSlotsValidator(CommanderValidator):

    def _validate(self):
        stats = self._entity.getStats()
        roster = self._entity.getRoster()
        pInfo = self._entity.getPlayerInfo()
        hasEmptySlots = roster.MAX_SLOTS > stats.readyCount + roster.MAX_EMPTY_SLOTS
        if hasEmptySlots or not pInfo.isReady:
            return ValidationResult(False, UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED)


class EventBattleSquadActionsValidator(SquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        return _EventBattleVehiclesValidator(entity)

    def _createSlotsValidator(self, entity):
        baseValidator = super(EventBattleSquadActionsValidator, self)._createSlotsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         baseValidator,
         EventSquadSlotsValidator(entity)])