# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/__init__.py
from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
from visual_script.contexts.perks_context import PerkContext, CrewContext, PerkNotifyState, CrewPerkLevelCollector
import ability_common, example, general, vehicle_blocks, qa_blocks, qa_education_blocks, balance, entity_blocks, arena_blocks, bitmask_blocks_common
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT, ASPECT.SERVER)
g_blockRegistrar.regBlocksFromModule(example)
g_blockRegistrar.regTypesFromModule(example)
g_blockRegistrar.regBlocksFromModule(qa_blocks)
g_blockRegistrar.regBlocksFromModule(qa_education_blocks)
g_blockRegistrar.regBlocksFromModule(balance)
g_blockRegistrar.regTypesFromModule(balance)
g_blockRegistrar.regBlocksFromModule(general)
g_blockRegistrar.regBlocksFromModule(vehicle_blocks)
g_blockRegistrar.regBlocksFromModule(ability_common)
g_blockRegistrar.regType(ability_common.Stage)
g_blockRegistrar.regType(ability_common.EquipmentErrorState)
g_blockRegistrar.regBlock(bitmask_blocks_common.BitwiseNOT)
g_blockRegistrar.regBlock(bitmask_blocks_common.BitwiseAND)
g_blockRegistrar.regBlock(bitmask_blocks_common.BitwiseOR)
g_blockRegistrar.regBlock(bitmask_blocks_common.BitwiseXOR)
g_blockRegistrar.regBlock(bitmask_blocks_common.BitwiseEQUAL)
g_blockRegistrar.regBlocksFromModule(entity_blocks)
g_blockRegistrar.regBlock(arena_blocks.GetFlyDirection)
g_blockRegistrar.regContext(PerkContext)
g_blockRegistrar.regContext(CrewContext)
g_blockRegistrar.regType(PerkNotifyState)
g_blockRegistrar.regType(CrewPerkLevelCollector)