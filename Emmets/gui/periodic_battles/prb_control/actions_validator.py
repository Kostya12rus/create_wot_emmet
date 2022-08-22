# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/periodic_battles/prb_control/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION, UNIT_RESTRICTION
from gui.periodic_battles.models import PrimeTimeStatus

class PrimeTimeValidator(BaseActionsValidator):
    _controller = None

    def _validate(self):
        if not self._controller.isBattlesPossible():
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NO_BATTLES, None)
        else:
            status, _, _ = self._controller.getPrimeTimeStatus()
            if status == PrimeTimeStatus.NOT_SET:
                return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_SET, None)
            if status != PrimeTimeStatus.AVAILABLE:
                return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE, None)
            return super(PrimeTimeValidator, self)._validate()


class SquadPrimeTimeValidator(UnitStateValidator):
    _controller = None

    def _validate(self):
        if not self._controller.isBattlesPossible():
            return ValidationResult(False, UNIT_RESTRICTION.MODE_NO_BATTLES, None)
        else:
            status, _, _ = self._controller.getPrimeTimeStatus()
            if status == PrimeTimeStatus.NOT_SET:
                return ValidationResult(False, UNIT_RESTRICTION.MODE_NOT_SET, None)
            if status != PrimeTimeStatus.AVAILABLE:
                return ValidationResult(False, UNIT_RESTRICTION.MODE_NOT_AVAILABLE, None)
            return super(SquadPrimeTimeValidator, self)._validate()