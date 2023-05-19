# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/header/battle_type_selector/pointcuts.py
from helpers import aop
import aspects

class _BattleItemSelector(aop.Pointcut):

    def __init__(self, battleTypeBuilderMethod, aspects_):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header', 'battle_selector_items', battleTypeBuilderMethod, aspects=aspects_)


class RankedBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addRankedBattleType', (
         aspects.RankedBattle,))


class CommandBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addCommandBattleType', (
         aspects.CommandBattle,))


class TrainingBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addTrainingBattleType', (
         aspects.TrainingBattle,))


class SpecialBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addSpecialBattleType', (
         aspects.SpecialBattle,))


class StrongholdBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addStrongholdsBattleType', (
         aspects.StrongholdBattle,))


class OnBattleTypeSelectorPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover', 'BattleTypeSelectPopover', '_populate', aspects=(
         aspects.OnBattleTypeSelectorPopulate,))