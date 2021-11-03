# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/__init__.py
from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
from constants import IS_DEVELOPMENT
import example, general, vehicle_blocks, qa_blocks, qa_education_blocks
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT, ASPECT.SERVER)
if IS_DEVELOPMENT:
    g_blockRegistrar.regBlocksFromModule(example)
    g_blockRegistrar.regTypesFromModule(example)
    g_blockRegistrar.regBlocksFromModule(qa_blocks)
    g_blockRegistrar.regBlocksFromModule(qa_education_blocks)
g_blockRegistrar.regBlocksFromModule(general)
g_blockRegistrar.regBlocksFromModule(vehicle_blocks)