# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/material_component.py
import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class MaterialComponent(object):
    category = 'Material'
    editorTitle = 'Material'
    domain = CGF.DomainOption.DomainAll
    kind = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Kind', value='', annotations={'comboBox': {'ground': 'ground', 'stone': 'stone', 
                    'wood': 'wood', 
                    'metal': 'metal', 
                    'snow': 'snow', 
                    'sand': 'sand', 
                    'water': 'water', 
                    'dirt': 'dirt', 
                    'oil': 'oil'}})