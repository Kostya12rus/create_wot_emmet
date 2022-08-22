# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/platoon_dropdown_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class PlatoonDropdownModel(ViewModel):
    __slots__ = ('onOutsideClick', )

    def __init__(self, properties=6, commands=1):
        super(PlatoonDropdownModel, self).__init__(properties=properties, commands=commands)

    @property
    def btnFind(self):
        return self._getViewModel(0)

    @staticmethod
    def getBtnFindType():
        return ButtonModel

    @property
    def btnCreate(self):
        return self._getViewModel(1)

    @staticmethod
    def getBtnCreateType():
        return ButtonModel

    def getBattleType(self):
        return self._getString(2)

    def setBattleType(self, value):
        self._setString(2, value)

    def getIsSettingsVisible(self):
        return self._getBool(3)

    def setIsSettingsVisible(self, value):
        self._setBool(3, value)

    def getIsRibbonVisible(self):
        return self._getBool(4)

    def setIsRibbonVisible(self, value):
        self._setBool(4, value)

    def getBackgroundImage(self):
        return self._getString(5)

    def setBackgroundImage(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(PlatoonDropdownModel, self)._initialize()
        self._addViewModelProperty('btnFind', ButtonModel())
        self._addViewModelProperty('btnCreate', ButtonModel())
        self._addStringProperty('battleType', '')
        self._addBoolProperty('isSettingsVisible', False)
        self._addBoolProperty('isRibbonVisible', False)
        self._addStringProperty('backgroundImage', '')
        self.onOutsideClick = self._addCommand('onOutsideClick')