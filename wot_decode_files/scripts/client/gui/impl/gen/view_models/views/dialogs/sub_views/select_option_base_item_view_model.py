# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_option_base_item_view_model.py
from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel

class ComponentType(Enum):
    BASE = 'base'
    MONEY = 'money'
    DEMOUNT_KIT = 'demountKit'


class SelectOptionBaseItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SelectOptionBaseItemViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def tooltip(self):
        return self._getViewModel(0)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getComponentType(self):
        return ComponentType(self._getString(1))

    def setComponentType(self, value):
        self._setString(1, value.value)

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)

    def _initialize(self):
        super(SelectOptionBaseItemViewModel, self)._initialize()
        self._addViewModelProperty('tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty('componentType')
        self._addBoolProperty('isDisabled', False)
        self._addResourceProperty('icon', R.invalid())