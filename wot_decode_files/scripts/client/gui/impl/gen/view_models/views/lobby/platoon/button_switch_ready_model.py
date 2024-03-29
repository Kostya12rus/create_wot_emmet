# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/button_switch_ready_model.py
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class ButtonSwitchReadyModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(ButtonSwitchReadyModel, self).__init__(properties=properties, commands=commands)

    def getIsRed(self):
        return self._getBool(6)

    def setIsRed(self, value):
        self._setBool(6, value)

    def getTooltipHeader(self):
        return self._getString(7)

    def setTooltipHeader(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(ButtonSwitchReadyModel, self)._initialize()
        self._addBoolProperty('isRed', False)
        self._addStringProperty('tooltipHeader', '')