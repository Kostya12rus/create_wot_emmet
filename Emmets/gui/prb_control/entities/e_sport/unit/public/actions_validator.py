# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/e_sport/unit/public/actions_validator.py
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.unit.actions_validator import UnitActionsValidator, UnitLevelsValidator, CommanderValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION

class ESportLevelsValidator(CommanderValidator):

    def _validate(self):
        stats = self._entity.getStats()
        levels = self._getInvalidLevels(stats)
        if stats.occupiedSlotsCount > 1 and stats.freeSlotsCount > 0 and levels:
            return ValidationResult(False, UNIT_RESTRICTION.INVALID_TOTAL_LEVEL, {'vehLevels': levels})
        return super(ESportLevelsValidator, self)._validate()

    def _getInvalidLevels(self, stats):
        rosterSettings = self._entity.getRosterSettings()
        maxLevel = rosterSettings.getMaxLevel()
        maxSlots = rosterSettings.getMaxSlots()
        maxTotalLevel = rosterSettings.getMaxTotalLevel()
        compensation = maxLevel * maxSlots - maxTotalLevel
        if compensation <= 0:
            return []
        levels = []
        for level in stats.levelsSeq:
            if not level:
                continue
            diff = maxLevel - level
            if diff:
                if level not in levels:
                    levels.append(level)
                if compensation > 0:
                    compensation -= diff
                else:
                    levels.sort()
                    return levels

        return []


class ESportSearchValidator(UnitLevelsValidator):

    def _validate(self):
        return ValidationResult(True, UNIT_RESTRICTION.NEED_PLAYERS_SEARCH)

    def _isEnabled(self):
        return not self._areVehiclesSelected(self._entity.getStats())


class ESportActionsValidator(UnitActionsValidator):

    def __init__(self, entity):
        super(ESportActionsValidator, self).__init__(entity)
        self.addWarning(ESportSearchValidator(entity))

    def _createLevelsValidator(self, entity):
        baseValidator = super(ESportActionsValidator, self)._createLevelsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[
         ESportLevelsValidator(entity),
         baseValidator])