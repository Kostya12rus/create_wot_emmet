# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/serialization/utils.py
from typing import Dict, Type
from .component_bin_deserializer import ComponentBinDeserializer
from .component_bin_serializer import ComponentBinSerializer
from .serializable_component import SerializableComponent, SerializableComponentChildType
__all__ = ('makeCompDescr', 'parseCompDescr')

def makeCompDescr(customizationItem):
    return ComponentBinSerializer().serialize(customizationItem)


def parseCompDescr(CUSTOMIZATION_CLASSES, customizationElementCompDescr):
    return ComponentBinDeserializer(CUSTOMIZATION_CLASSES).decode(customizationElementCompDescr)