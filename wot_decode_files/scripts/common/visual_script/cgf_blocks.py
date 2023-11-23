# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/cgf_blocks.py
from visual_script.block import Meta
from visual_script.misc import ASPECT

class CGFMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16540163

    @classmethod
    def blockCategory(cls):
        return 'CGF'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/cgf'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR, ASPECT.SERVER]