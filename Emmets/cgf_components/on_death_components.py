# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/on_death_components.py
import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class ChangeModelOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Change Model On Death Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    modelPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Model path', annotations={'path': '*.model'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='Delay', value=0.0)

    def __init__(self):
        self.initialModel = None
        return


@registerComponent
class SoundOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Sound On Death Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    soundPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Sound Prefab', annotations={'path': '*.prefab'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGFMetaTypes.BOOL, editorName='Attach to GO', value=True)


@registerComponent
class EffectOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Effect On Death Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Effect Prefab', annotations={'path': '*.prefab'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGFMetaTypes.BOOL, editorName='Attach to GO', value=True)