# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/resource_well/tooltips/refund_resources_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.resource_well.tooltips.refund_resources_tooltip_model import RefundResourcesTooltipModel
from gui.impl.pub import ViewImpl
from uilogging.resource_well.loggers import ResourceWellReturnTooltipLogger

class RefundResourcesTooltip(ViewImpl):
    __slots__ = ()
    __uiLogger = ResourceWellReturnTooltipLogger()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.resource_well.tooltips.RefundResourcesTooltip())
        settings.model = RefundResourcesTooltipModel()
        super(RefundResourcesTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RefundResourcesTooltip, self).getViewModel()

    def _onLoaded(self, *args, **kwargs):
        super(RefundResourcesTooltip, self)._onLoaded(*args, **kwargs)
        self.__uiLogger.onTooltipOpened()

    def _finalize(self):
        self.__uiLogger.onTooltipClosed()
        super(RefundResourcesTooltip, self)._finalize()