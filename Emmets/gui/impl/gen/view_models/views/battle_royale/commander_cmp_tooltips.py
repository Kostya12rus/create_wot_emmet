# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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