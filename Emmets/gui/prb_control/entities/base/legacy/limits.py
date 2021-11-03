# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/legacy/limits.py
from gui.prb_control.entities.base.limits import LimitsCollection, VehicleIsValid, TeamIsValid

class LegacyLimits(LimitsCollection):

    def __init__(self, entity):
        super(LegacyLimits, self).__init__(entity, (VehicleIsValid(),), (TeamIsValid(),))