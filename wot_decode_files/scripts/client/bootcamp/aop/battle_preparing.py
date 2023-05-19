# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/aop/battle_preparing.py
from helpers import aop
from bootcamp.aop import common

def weave(weaver, stateBattlePreparing):
    weaver.weave(pointcut=_PointcutDelayStartFirstBattle(stateBattlePreparing))


class _PointcutDelayStartFirstBattle(aop.Pointcut):

    def __init__(self, stateBattlePreparing):
        super(_PointcutDelayStartFirstBattle, self).__init__('Avatar', 'PlayerAvatar', '^(vehicle_onAppearanceReady|onEnterWorld|onSpaceLoaded)$', aspects=(
         common.AspectRedirectMethod({'vehicle_onAppearanceReady': stateBattlePreparing.onVehicleOnAppearanceReady, 
            'onEnterWorld': stateBattlePreparing.onAvatarOnEnterWorld, 
            'onSpaceLoaded': stateBattlePreparing.onSpaceLoaded}),))