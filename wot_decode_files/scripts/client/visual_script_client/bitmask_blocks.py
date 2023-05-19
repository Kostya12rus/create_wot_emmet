# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/bitmask_blocks.py
from visual_script.bitmask_blocks_common import BitMaskBase
from visual_script.misc import ASPECT
from constants import EQUIPMENT_ERROR_STATES

class BitMask(BitMaskBase):
    _MASK_TYPES = {'Equipment ErrorStates': EQUIPMENT_ERROR_STATES}

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]