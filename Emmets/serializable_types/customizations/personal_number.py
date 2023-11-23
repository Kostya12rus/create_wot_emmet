# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/serializable_types/customizations/personal_number.py
from collections import OrderedDict
from items.components.c11n_constants import ApplyArea
from serialization.field import intField, strField, applyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = ('PersonalNumberComponent', )

class PersonalNumberComponent(SerializableComponent):
    __metaclass__ = ReflectionMetaclass
    customType = C11nSerializationTypes.PERSONAL_NUMBER
    fields = OrderedDict((
     (
      'id', intField()),
     (
      'number', strField()),
     (
      'appliedTo', applyAreaEnumField(ApplyArea.NONE))))
    __slots__ = ('id', 'number', 'appliedTo')

    def __init__(self, id=0, number=None, appliedTo=ApplyArea.NONE):
        self.id = id
        self.number = number or ''
        self.appliedTo = appliedTo
        super(PersonalNumberComponent, self).__init__()

    def isFilled(self):
        return bool(self.number)