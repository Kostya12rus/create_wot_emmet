# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/vehicle_roles.py
from gui.shared.tooltips import ToolTipBaseData
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView

class VehicleRolesTooltipContentWindowData(ToolTipBaseData):

    def __init__(self, context):
        super(VehicleRolesTooltipContentWindowData, self).__init__(context, TOOLTIPS_CONSTANTS.VEHICLE_ROLES)

    def getDisplayableData(self, vehicleCD, *args, **kwargs):
        return DecoratedTooltipWindow(VehicleRolesTooltipView(vehicleCD), useDecorator=False)