# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/ability_common.py
import typing
from visual_script.type import VScriptEnum
from constants import EQUIPMENT_STAGES, EQUIPMENT_ERROR_STATES

class Stage(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return 'EquipmentStagesT'

    @classmethod
    def vs_enum(cls):
        return EQUIPMENT_STAGES


class EquipmentErrorState(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return 'EquipmentErrorStatesT'

    @classmethod
    def vs_enum(cls):
        return EQUIPMENT_ERROR_STATES