# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/serializable_types/customizations/decal.py
from collections import OrderedDict
from items.components.c11n_constants import ApplyArea
from serialization.field import intField, applyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = ('DecalComponent', )

class DecalComponent(SerializableComponent):
    __metaclass__ = ReflectionMetaclass
    customType = C11nSerializationTypes.DECAL
    fields = OrderedDict((
     (
      'id', intField()),
     (
      'appliedTo', applyAreaEnumField(ApplyArea.NONE)),
     (
      'progressionLevel', intField(0))))
    __slots__ = ('id', 'appliedTo', 'progressionLevel')

    def __init__(self, id=0, appliedTo=ApplyArea.NONE, progressionLevel=0):
        self.id = id
        self.appliedTo = appliedTo
        self.progressionLevel = progressionLevel
        super(DecalComponent, self).__init__()