# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/advanced_tooltip_view_model.py
from frameworks.wulf import ViewModel

class AdvancedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AdvancedTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getMovie(self):
        return self._getString(0)

    def setMovie(self, value):
        self._setString(0, value)

    def getHeader(self):
        return self._getString(1)

    def setHeader(self, value):
        self._setString(1, value)

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(AdvancedTooltipViewModel, self)._initialize()
        self._addStringProperty('movie', '')
        self._addStringProperty('header', '')
        self._addStringProperty('description', '')