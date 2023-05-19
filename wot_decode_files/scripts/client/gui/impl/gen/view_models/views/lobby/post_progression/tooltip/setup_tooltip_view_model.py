# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/setup_tooltip_view_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.feature_tooltip_view_model import FeatureTooltipViewModel

class SetupFeatureType(Enum):
    SHELLSCONSUMABLESSWITCH = 'shells_consumables_switch'
    OPTDEVBOOSTERSSWITCH = 'opt_dev_boosters_switch'


class SetupTooltipViewModel(FeatureTooltipViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SetupTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getIconName(self):
        return self._getString(3)

    def setIconName(self, value):
        self._setString(3, value)

    def getType(self):
        return SetupFeatureType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(SetupTooltipViewModel, self)._initialize()
        self._addStringProperty('iconName', '')
        self._addStringProperty('type')