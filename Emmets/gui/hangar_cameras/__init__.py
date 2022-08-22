# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cameras/__init__.py
from skeletons.gui.hangar_cameras import IHangarCameraSounds
__all__ = ('getHangarCamerasConfig', )

def getHangarCamerasConfig(manager):
    from gui.hangar_cameras.hangar_camera_sounds import HangarCameraSounds
    ctrl = HangarCameraSounds()
    ctrl.init()
    manager.addInstance(IHangarCameraSounds, ctrl, finalizer='fini')