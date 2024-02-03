# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/hangar_rules.py
import CGF
from cgf_components.tooltip_component import TooltipManager
from cgf_components.trigger_vse_component import TriggerVSEComponentsManager
from cgf_components.token_component import TokenManager
from cgf_script.managers_registrator import registerManager, Rule, registerRule
from hover_component import HoverManager
from highlight_component import HighlightManager
from on_click_components import ClickManager
from hangar_camera_manager import HangarCameraManager

@registerRule
class SelectionRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(HoverManager)
    def reg1(self):
        return

    @registerManager(HighlightManager)
    def reg2(self):
        return

    @registerManager(ClickManager)
    def reg3(self):
        return

    @registerManager(TooltipManager)
    def reg4(self):
        return


@registerRule
class CameraRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(HangarCameraManager)
    def reg1(self):
        return


@registerRule
class HangarTokenRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(TokenManager)
    def reg1(self):
        return

    @registerManager(TriggerVSEComponentsManager)
    def reg2(self):
        return