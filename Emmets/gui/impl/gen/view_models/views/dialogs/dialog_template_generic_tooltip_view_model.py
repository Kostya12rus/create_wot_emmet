# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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