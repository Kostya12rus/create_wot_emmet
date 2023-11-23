# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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