# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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