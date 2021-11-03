# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/customization/__init__.py
from collections import namedtuple
CustomizationTooltipContext = namedtuple('CustomizationTooltipContext', ('itemCD',
                                                                         'vehicleIntCD',
                                                                         'showInventoryBlock',
                                                                         'level',
                                                                         'showOnlyProgressBlock',
                                                                         'customVehicleCD'))
CustomizationTooltipContext.__new__.__defaults__ = (
 -1, -1, False, -1, False)