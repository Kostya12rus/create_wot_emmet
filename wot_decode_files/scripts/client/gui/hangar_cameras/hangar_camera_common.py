# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cameras/hangar_camera_common.py
from enum import Enum
from gui.shared.events import HasCtxEvent

class CameraMovementStates(object):
    ON_OBJECT = 0
    MOVING_TO_OBJECT = 1
    FROM_OBJECT = 2


class CameraDistanceModes(Enum):
    DEFAULT = 0
    CUSTOM = 1


class CameraRelatedEvents(HasCtxEvent):
    CAMERA_ENTITY_UPDATED = 'CameraEntityUpdate'
    IDLE_CAMERA = 'IdleCamera'
    VEHICLE_LOADING = 'VehicleLoading'
    LOBBY_VIEW_MOUSE_MOVE = 'MouseMove'
    FORCE_DISABLE_IDLE_PARALAX_MOVEMENT = 'cameraRelatedEvents/forceDisableIdleParalaxMovement'
    FORCE_DISABLE_CAMERA_MOVEMENT = 'cameraRelatedEvents/forceDisableCameraMovement'