# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/on_shot_components.py
import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from vehicle_systems.model_assembler import loadAppearancePrefab

@registerComponent
class EffectOnShotComponent(object):
    category = 'Shooting'
    editorTitle = 'Effect On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Effect Prefab', annotations={'path': '*.prefab'})


@registerComponent
class SoundOnShotComponent(object):
    category = 'Shooting'
    editorTitle = 'Sound On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    soundPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Sound Prefab', annotations={'path': '*.prefab'})


@registerComponent
class ShellCasingsEjectionController(object):

    def __init__(self, appearance, shellCasingsEjectionPrefab):
        loadAppearancePrefab(shellCasingsEjectionPrefab, appearance)