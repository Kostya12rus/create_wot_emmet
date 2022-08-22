# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_modifiers/helpers.py
from typing import TYPE_CHECKING
from gui.impl.lobby.battle_modifiers.constants import MOD_TYPE_MAP, PHYS_TYPE_MAP, USE_TYPE_MAP, GAMEPLAY_IMPACT_MAP
from gui.impl.gen.view_models.views.lobby.battle_modifiers.modifier_model import ModifierModel
if TYPE_CHECKING:
    from battle_modifiers.battle_modifiers import BattleModifier

def packModifierModel(modifier):
    result = ModifierModel()
    result.setValue(modifier.value)
    result.setUseType(USE_TYPE_MAP[modifier.useType])
    result.setModificationType(MOD_TYPE_MAP[modifier.param.id])
    result.setPhysicalType(PHYS_TYPE_MAP[modifier.param.clientData.physicalType])
    result.setGameplayImpact(GAMEPLAY_IMPACT_MAP[modifier.gameplayImpact])
    return result