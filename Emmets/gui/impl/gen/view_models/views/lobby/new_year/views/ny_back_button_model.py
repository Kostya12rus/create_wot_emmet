# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/views/ny_back_button_model.py
from frameworks.wulf import ViewModel

class NyBackButtonModel(ViewModel):
    __slots__ = ('onBack', )

    def __init__(self, properties=3, commands=1):
        super(NyBackButtonModel, self).__init__(properties=properties, commands=commands)

    def getIsVisible(self):
        return self._getBool(0)

    def setIsVisible(self, value):
        self._setBool(0, value)

    def getCaption(self):
        return self._getString(1)

    def setCaption(self, value):
        self._setString(1, value)

    def getGoTo(self):
        return self._getString(2)

    def setGoTo(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(NyBackButtonModel, self)._initialize()
        self._addBoolProperty('isVisible', False)
        self._addStringProperty('caption', '')
        self._addStringProperty('goTo', '')
        self.onBack = self._addCommand('onBack')