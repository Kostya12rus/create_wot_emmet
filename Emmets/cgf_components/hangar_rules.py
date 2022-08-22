# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/hangar_rules.py
from cgf_script.managers_registrator import registerManager, Rule
from hover_component import HoverManager
from highlight_component import HighlightManager
from on_click_components import ClickManager

class SelectionRule(Rule):
    category = 'Hangar rules'

    @registerManager(HoverManager)
    def reg1(self):
        return

    @registerManager(HighlightManager)
    def reg2(self):
        return

    @registerManager(ClickManager)
    def reg3(self):
        return