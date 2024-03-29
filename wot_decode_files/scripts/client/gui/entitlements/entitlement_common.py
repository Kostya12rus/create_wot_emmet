# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/entitlements/entitlement_common.py
import typing
from helpers import dependency
from skeletons.gui.game_control import IEventLootBoxesController
if typing.TYPE_CHECKING:
    from typing import FrozenSet, Generator, Type
    from skeletons.gui.game_control import IEntitlementsConsumer
LOOT_BOX_COUNTER_ENTITLEMENT = 'loot_box_counter'
ENTITLEMENTS = (
 LOOT_BOX_COUNTER_ENTITLEMENT,)
_CONSUMERS = frozenset((
 IEventLootBoxesController,))

def iterConsumers():
    return (dependency.instance(iConsumer) for iConsumer in _CONSUMERS)