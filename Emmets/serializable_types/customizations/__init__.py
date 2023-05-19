# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/serializable_types/customizations/__init__.py
from serialization import parseCompDescr
from serialization.serializable_component import SerializableComponentChildType
from .attachment import AttachmentComponent
from .camouflage import CamouflageComponent
from .customization_outfit import CustomizationOutfit, getAllItemsFromOutfit
from .decal import DecalComponent
from .insignia import InsigniaComponent
from .paint import PaintComponent
from .personal_number import PersonalNumberComponent
from .projection_decal import ProjectionDecalComponent
from .sequence import SequenceComponent
__all__ = ('AttachmentComponent', 'CamouflageComponent', 'CustomizationOutfit', 'getAllItemsFromOutfit',
           'DecalComponent', 'InsigniaComponent', 'PaintComponent', 'PersonalNumberComponent',
           'ProjectionDecalComponent', 'SequenceComponent', 'CUSTOMIZATION_CLASSES',
           'parseC11sComponentDescr')
CUSTOMIZATION_CLASS_LIST = [
 AttachmentComponent, 
 CamouflageComponent, 
 CustomizationOutfit, 
 DecalComponent, 
 InsigniaComponent, 
 PaintComponent, 
 PersonalNumberComponent, 
 ProjectionDecalComponent, 
 SequenceComponent]
CUSTOMIZATION_CLASSES = {subClass.customType: subClass for subClass in CUSTOMIZATION_CLASS_LIST}

def parseC11sComponentDescr(customizationElementCompDescr):
    return parseCompDescr(CUSTOMIZATION_CLASSES, customizationElementCompDescr)