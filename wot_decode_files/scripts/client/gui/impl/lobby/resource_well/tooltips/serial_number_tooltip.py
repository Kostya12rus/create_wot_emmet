# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/resource_well/tooltips/serial_number_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.resource_well.tooltips.serial_number_tooltip_model import SerialNumberTooltipModel
from gui.impl.pub import ViewImpl

class SerialNumberTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.resource_well.tooltips.SerialNumberTooltip())
        settings.model = SerialNumberTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(SerialNumberTooltip, self).__init__(settings)