# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/commander_cmp_tooltips.py
from frameworks.wulf import ViewModel

class CommanderCmpTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_SIXTH_SENSE_SKILL = 'commander_sixthSense'
    TOOLTIP_EXPERT_SKILL = 'commander_expert'
    TOOLTIP_TANKMAN = 'battleRoyaleTankman'

    def __init__(self, properties=0, commands=0):
        super(CommanderCmpTooltips, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CommanderCmpTooltips, self)._initialize()