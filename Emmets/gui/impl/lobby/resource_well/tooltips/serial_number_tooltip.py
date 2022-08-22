# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/resource_well/tooltips/serial_number_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.resource_well.tooltips.serial_number_tooltip_model import SerialNumberTooltipModel
from gui.impl.pub import ViewImpl
from uilogging.resource_well.loggers import ResourceWellSerialNumberTooltipLogger

class SerialNumberTooltip(ViewImpl):
    __slots__ = ()
    __uiLogger = ResourceWellSerialNumberTooltipLogger()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.resource_well.tooltips.SerialNumberTooltip())
        settings.model = SerialNumberTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(SerialNumberTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SerialNumberTooltip, self).getViewModel()

    def _onLoaded(self, parentLayout, *args, **kwargs):
        super(SerialNumberTooltip, self)._onLoaded(*args, **kwargs)
        self.__uiLogger.onTooltipOpened(layoutID=parentLayout)

    def _finalize(self):
        self.__uiLogger.onTooltipClosed()
        super(SerialNumberTooltip, self)._finalize()