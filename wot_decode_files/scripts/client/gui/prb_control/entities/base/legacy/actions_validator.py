# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/legacy/actions_validator.py
from PlayerEvents import g_playerEvents
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PREBATTLE_RESTRICTION
from prebattle_shared import decodeRoster

class InQueueValidator(BaseActionsValidator):

    def _validate(self):
        if g_playerEvents.isPlayerEntityChanging:
            return ValidationResult(False, PREBATTLE_RESTRICTION.TEAM_IS_IN_QUEUE)
        _, assigned = decodeRoster(self._entity.getRosterKey())
        if self._entity.getTeamState().isInQueue() and assigned:
            return ValidationResult(False, PREBATTLE_RESTRICTION.TEAM_IS_IN_QUEUE)
        return super(InQueueValidator, self)._validate()


class LegacyVehicleValid(BaseActionsValidator):

    def _validate(self):
        return self._entity.getLimits().isVehicleValid()


class LegacyTeamValidator(BaseActionsValidator):

    def _validate(self):
        return self._entity.getLimits().isTeamValid()

    def _isEnabled(self):
        return self._entity.isCommander()


class LegacyActionsValidator(ActionsValidatorComposite):

    def __init__(self, entity):
        validators = [
         InQueueValidator(entity),
         LegacyVehicleValid(entity),
         LegacyTeamValidator(entity)]
        super(LegacyActionsValidator, self).__init__(entity, validators)