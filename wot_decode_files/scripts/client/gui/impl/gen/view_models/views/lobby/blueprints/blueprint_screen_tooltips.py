# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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