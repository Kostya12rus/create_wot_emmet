# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/subfilters_constants.py


class AVATAR_SUBFILTERS(object):
    CAMERA_SHOT_POINT = 0
    CAMERA_ARTY_SHOT_POINT = 1
    CAMERA_ARTY_TRANSLATION = 2
    CAMERA_ARTY_ROTATION = 3


class FILTER_INTERPOLATION_TYPE(object):
    LINEAR = 0
    SLERP_OF_CARTESIAN = 1
    ANGLE_RADIANS = 2
    SPHERICAL_RADIANS = 3