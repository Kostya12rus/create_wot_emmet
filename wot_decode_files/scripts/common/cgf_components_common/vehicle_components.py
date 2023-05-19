# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/vehicle_components.py
import CGF, Triggers
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class VehicleDestroyingComponent(object):
    category = 'Vehicle'
    editorTitle = 'Vehicle Destroying Component'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionID = None
        return