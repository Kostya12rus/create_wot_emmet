# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/points_of_interest/registrars.py
import CGF
from cgf_script.managers_registrator import Rule, registerManager, registerRule
from points_of_interest.managers import PoiStateManager, PoiViewStateManager, PoiSoundManager

@registerRule
class PointsOfInterestRule(Rule):
    category = 'Points Of Interest'
    domain = CGF.DomainOption.DomainAll

    @registerManager(PoiStateManager)
    def registerPoiStateManager(self):
        return

    @registerManager(PoiViewStateManager)
    def registerPoiViewStateManager(self):
        return

    @registerManager(PoiSoundManager)
    def registerPoiSoundManager(self):
        return