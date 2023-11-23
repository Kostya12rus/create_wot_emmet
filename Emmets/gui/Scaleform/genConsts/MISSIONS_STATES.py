# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/MISSIONS_STATES.py


class MISSIONS_STATES(object):
    COMPLETED = 'done'
    FULL_COMPLETED = 'fullDone'
    NOT_AVAILABLE = 'notAvailable'
    WRONG_TIME = 'wrongTime'
    NONE = ''
    IN_PROGRESS = 'inProgress'
    DISABLED = 'disabled'
    IS_ON_PAUSE = 'isOnPause'
    EVENT_STATUS = [COMPLETED, FULL_COMPLETED, NOT_AVAILABLE, WRONG_TIME, NONE, IN_PROGRESS, 
     DISABLED, IS_ON_PAUSE]