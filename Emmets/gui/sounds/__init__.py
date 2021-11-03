# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/__init__.py
from gui.sounds.event_hangar_sound_ctrl import EventHangarSoundEnvController
from gui.sounds.sounds_ctrl import SoundsController
from skeletons.gui.event_hangar_sound import IEventHangarSoundEnv
from skeletons.gui.sounds import ISoundsController
__all__ = ('getSoundsConfig', )

def getSoundsConfig(manager):
    ctrl = SoundsController()
    ctrl.init()
    manager.addInstance(ISoundsController, ctrl, finalizer='fini')
    ctrl = EventHangarSoundEnvController()
    ctrl.init()
    manager.addInstance(IEventHangarSoundEnv, ctrl, finalizer='fini')