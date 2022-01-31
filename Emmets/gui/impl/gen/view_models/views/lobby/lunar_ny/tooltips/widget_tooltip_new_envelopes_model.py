# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lunar_ny/tooltips/widget_tooltip_new_envelopes_model.py
from frameworks.wulf import ViewModel

class WidgetTooltipNewEnvelopesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(WidgetTooltipNewEnvelopesModel, self).__init__(properties=properties, commands=commands)

    def getSecretSantaSentLimitTime(self):
        return self._getNumber(0)

    def setSecretSantaSentLimitTime(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(WidgetTooltipNewEnvelopesModel, self)._initialize()
        self._addNumberProperty('secretSantaSentLimitTime', 0)