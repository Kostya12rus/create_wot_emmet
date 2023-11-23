# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/bitmask_blocks.py
from visual_script.bitmask_blocks_common import BitMaskBase
from visual_script.misc import ASPECT
from constants import EQUIPMENT_ERROR_STATES, CollisionFlags

class BitMask(BitMaskBase):
    _MASK_TYPES = {'Equipment ErrorStates': EQUIPMENT_ERROR_STATES, 
       'Collision Flags': CollisionFlags}

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]