# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/dismissed_toggle_tooltip_model.py
from gui.impl.gen.view_models.views.lobby.crew.common.tankman_restore_info import TankmanRestoreInfo

class DismissedToggleTooltipModel(TankmanRestoreInfo):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DismissedToggleTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DismissedToggleTooltipModel, self)._initialize()