# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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