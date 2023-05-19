# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_template_generic_tooltip_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class TooltipType(Enum):
    BACKPORT = 'backport'
    NORMAL = 'normal'
    ABSENT = 'absent'


class DialogTemplateGenericTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(DialogTemplateGenericTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return TooltipType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(DialogTemplateGenericTooltipViewModel, self)._initialize()
        self._addStringProperty('type')