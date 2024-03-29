# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/button_model.py
from frameworks.wulf import ViewModel

class ButtonModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=6, commands=1):
        super(ButtonModel, self).__init__(properties=properties, commands=commands)

    def getCaption(self):
        return self._getString(0)

    def setCaption(self, value):
        self._setString(0, value)

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)

    def getHasTooltip(self):
        return self._getBool(3)

    def setHasTooltip(self, value):
        self._setBool(3, value)

    def getText(self):
        return self._getString(4)

    def setText(self, value):
        self._setString(4, value)

    def getTooltipCaption(self):
        return self._getString(5)

    def setTooltipCaption(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(ButtonModel, self)._initialize()
        self._addStringProperty('caption', '')
        self._addBoolProperty('isEnabled', True)
        self._addStringProperty('description', '')
        self._addBoolProperty('hasTooltip', True)
        self._addStringProperty('text', '')
        self._addStringProperty('tooltipCaption', '')
        self.onClick = self._addCommand('onClick')