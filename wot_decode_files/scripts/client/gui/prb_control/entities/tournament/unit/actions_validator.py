# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/tournament/unit/actions_validator.py
from gui.prb_control.entities.base.squad.actions_validator import UnitActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitVehiclesValidator, CommanderValidator, UnitStateValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION

class TournamentVehiclesValidator(UnitVehiclesValidator):
    pass


class TournamentUnitSlotsValidator(CommanderValidator):

    def _validate(self):
        rosterSettings = self._entity.getRosterSettings()
        stats = self._entity.getStats()
        isPlayersMatchingAvailable = self._entity.isPlayersMatchingAvailable()
        allMembersReady = stats.readyCount == stats.occupiedSlotsCount
        if isPlayersMatchingAvailable:
            isClanMembersEnough = stats.clanMembersInRoster >= rosterSettings.getMinClanMembersCount()
            if not isClanMembersEnough:
                return ValidationResult(False, UNIT_RESTRICTION.UNIT_MIN_CLAN_MEMBERS)
            if not allMembersReady:
                return ValidationResult(False, UNIT_RESTRICTION.NOT_READY_IN_SLOTS)
            if stats.occupiedSlotsCount < rosterSettings.getMaxSlots() + 1:
                return ValidationResult(True, UNIT_RESTRICTION.UNIT_WILL_SEARCH_PLAYERS)
        else:
            if rosterSettings.getMinSlots() > stats.occupiedSlotsCount:
                return ValidationResult(False, UNIT_RESTRICTION.MIN_SLOTS)
            if not allMembersReady:
                return ValidationResult(False, UNIT_RESTRICTION.NOT_READY_IN_SLOTS)
        return super(TournamentUnitSlotsValidator, self)._validate()


class TournamentUnitStateValidator(UnitStateValidator):

    def _validate(self):
        if self._entity.inPlayersMatchingMode():
            return ValidationResult(False, UNIT_RESTRICTION.UNIT_IS_IN_PLAYERS_MATCHING)
        return super(TournamentUnitStateValidator, self)._validate()


class TournamentActionsValidator(UnitActionsValidator):

    def _createVehiclesValidator(self, entity):
        return TournamentVehiclesValidator(entity)

    def _createSlotsValidator(self, entity):
        return TournamentUnitSlotsValidator(entity)

    def _createStateValidator(self, entity):
        return TournamentUnitStateValidator(entity)