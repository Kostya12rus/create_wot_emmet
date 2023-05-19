# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dog_tags_common/components_packer.py
import typing
if typing.TYPE_CHECKING:
    from typing import Tuple
_MASK_ID = 4294967295
_MASK_GRADE = 1099511627775 - _MASK_ID
_MASK_TEAM = 281474976710655 - _MASK_GRADE - _MASK_ID

def pack_component(compId, grade, team=0):
    p_grade = grade << 32 & _MASK_GRADE
    p_team = team << 40 & _MASK_TEAM
    p_id = compId & _MASK_ID
    return p_grade | p_team | p_id


def unpack_component(packed):
    team = int((packed & _MASK_TEAM) >> 40)
    grade = int((packed & _MASK_GRADE) >> 32)
    compId = int(packed & _MASK_ID)
    return (compId, grade, team)