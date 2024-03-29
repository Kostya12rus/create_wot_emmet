# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_template_button_view_model.py
from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel

class ButtonType(Enum):
    MAIN = 'main'
    PRIMARY = 'primary'
    PRIMARY_GREEN = 'primaryGreen'
    PRIMARY_RED = 'primaryRed'
    SECONDARY = 'secondary'
    GHOST = 'ghost'


class DialogTemplateButtonViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DialogTemplateButtonViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def tooltip(self):
        return self._getViewModel(0)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getButtonID(self):
        return self._getString(1)

    def setButtonID(self, value):
        self._setString(1, value)

    def getLabel(self):
        return self._getResource(2)

    def setLabel(self, value):
        self._setResource(2, value)

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)

    def getType(self):
        return ButtonType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(DialogTemplateButtonViewModel, self)._initialize()
        self._addViewModelProperty('tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty('buttonID', '')
        self._addResourceProperty('label', R.invalid())
        self._addBoolProperty('isDisabled', False)
        self._addStringProperty('type')