# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/hangar_rules.py
import CGF
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


@registerRule
class CameraRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(HangarCameraManager)
    def reg1(self):
        return