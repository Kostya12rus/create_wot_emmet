# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/cond_formatters/vehicle.py
from gui.server_events.cond_formatters.formatters import MissionsBattleConditionsFormatter, EmptyMissionsFormatter

class MissionsVehicleConditionsFormatter(MissionsBattleConditionsFormatter):

    def __init__(self):
        super(MissionsVehicleConditionsFormatter, self).__init__({'customization': _CustomizationFormatter()})


class _CustomizationFormatter(EmptyMissionsFormatter):
    pass