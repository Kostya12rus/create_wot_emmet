# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_screen_tooltips.py
from frameworks.wulf import ViewModel

class BlueprintScreenTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_XP_DISCOUNT = 'BLUEPRINTS_TOOLTIP_XP_DISCOUNT'
    TOOLTIP_BLUEPRINT = 'TOOLTIP_BLUEPRINT'
    TOOLTIP_BLUEPRINT_ITEM_PLACE = 'TOOLTIP_BLUEPRINT_ITEM_PLACE'
    TOOLTIP_BLUEPRINT_CONVERT_COUNT = 'TOOLTIP_BLUEPRINT_CONVERT_COUNT'

    def __init__(self, properties=0, commands=0):
        super(BlueprintScreenTooltips, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(BlueprintScreenTooltips, self)._initialize()