# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/markers2d/settings.py
from enum import IntEnum
from Math import Vector3
from gui.shared import EVENT_BUS_SCOPE
SCOPE = EVENT_BUS_SCOPE.BATTLE
MARKER_POSITION_ADJUSTMENT = Vector3(0.0, 12.0, 0.0)
MARKERS_COLOR_SCHEME_PREFIX = 'vm_'

class MARKER_SYMBOL_NAME(object):
    VEHICLE_MARKER = 'VehicleMarker'
    TARGET_MARKER = 'TargetMarker'
    EQUIPMENT_MARKER = 'FortConsumablesMarker'
    LOCATION_MARKER = 'LocationMarkerUI'
    ATTENTION_MARKER = 'AttentionMarkerUI'
    SHOOTING_MARKER = 'AimMarkerUI'
    NAVIGATION_MARKER = 'NavigationMarkerUI'
    SAFE_ZONE_MARKER = 'SafeZoneIndicatorUI'
    STATIC_OBJECT_MARKER = 'StaticObjectMarker'
    STATIC_ARTY_MARKER = 'StaticArtyMarkerUI'
    SECTOR_BASE_TYPE = 'SectorBaseMarkerUI'
    HEADQUARTER_TYPE = 'HeadquarterMarkerUI'
    STEP_REPAIR_MARKER_TYPE = 'ResupplyMarkerUI'
    WAYPOINT_MARKER = 'SectorWaypointMarkerUI'
    SECTOR_WARNING_MARKER = 'SectorWarningMarkerUI'


class DAMAGE_TYPE(object):
    FROM_UNKNOWN = 0
    FROM_ALLY = 1
    FROM_ENEMY = 2
    FROM_SQUAD = 3
    FROM_PLAYER = 4


class CommonMarkerType(IntEnum):
    NORMAL = 0
    BASE = 1
    FRONTLINE_BASE = 2
    FRONTLINE_WAYPOINT = 3
    FRONTLINE_HEADQUARTER = 4
    FRONTLINE_WARNING = 5
    LOCATION = 6
    VEHICLE = 7