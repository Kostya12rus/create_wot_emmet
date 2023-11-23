# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/vehicle_collector_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, vehicle_collector
from gui.shared.tooltips.builders import DataBuilder, DefaultFormatBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.VEHICLE_COLLECTOR_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, vehicle_collector.VehicleCollectorTooltipData(contexts.ToolTipContext(None))),
     DefaultFormatBuilder(TOOLTIPS_CONSTANTS.VEHICLE_COLLECTOR_DISABLED, TOOLTIPS_CONSTANTS.COMPLEX_UI, vehicle_collector.VehicleCollectorDisabledTooltipData(contexts.ToolTipContext(None))))