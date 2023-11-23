# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/tooltips/mode_selector_alert_tooltip.py
from gui.impl.gen import R
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.windows.simple_tooltip_content_model import SimpleTooltipContentModel
from gui.impl.pub import ViewImpl

class AlertTooltip(ViewImpl):

    def __init__(self, header, body, alert):
        self.__header = header
        self.__body = body
        self.__alert = alert
        settings = ViewSettings(R.views.lobby.mode_selector.tooltips.AlertTooltip(), model=SimpleTooltipContentModel())
        super(AlertTooltip, self).__init__(settings)

    def _onLoading(self, *args, **kwargs):
        model = self.getViewModel()
        model.setHeader(self.__header)
        model.setBody(self.__body)
        model.setAlert(self.__alert)