# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/mute_all_toggle_model.py
from frameworks.wulf import ViewModel

class MuteAllToggleModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=4, commands=1):
        super(MuteAllToggleModel, self).__init__(properties=properties, commands=commands)

    def getTooltipHeader(self):
        return self._getString(0)

    def setTooltipHeader(self, value):
        self._setString(0, value)

    def getTooltipBody(self):
        return self._getString(1)

    def setTooltipBody(self, value):
        self._setString(1, value)

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(MuteAllToggleModel, self)._initialize()
        self._addStringProperty('tooltipHeader', '')
        self._addStringProperty('tooltipBody', '')
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isVisible', True)
        self.onClick = self._addCommand('onClick')