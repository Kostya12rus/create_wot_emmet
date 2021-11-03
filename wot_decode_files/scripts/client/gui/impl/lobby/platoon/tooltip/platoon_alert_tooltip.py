# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/platoon/tooltip/platoon_alert_tooltip.py
from gui.impl.gen import R
from gui.impl import backport
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.lobby.platoon.alert_tooltip_model import AlertTooltipModel

class AlertTooltip(ViewImpl):

    def __init__(self, header, body):
        self.__header = header
        self.__body = body
        settings = ViewSettings(R.views.lobby.platoon.AlertTooltip(), model=AlertTooltipModel())
        super(AlertTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (model):
            model.setHeader(backport.text(self.__header))
            model.setBody(backport.text(self.__body))