# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/shot_color_transmission_component.py
import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class ShotColorTransmissionComponent(object):
    editorTitle = 'Gun Shot Effect Component'
    category = 'Animator Triggers'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    materialParam = ComponentProperty(type=CGFMetaTypes.STRING, editorName='material property', value='TintColor')
    startValue = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='start value', value=0.0)
    endValue = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='end value', value=0.5)