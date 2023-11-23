# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/permissions.py
from gui.prb_control.entities.base.permissions import IPrbPermissions

class PreQueuePermissions(IPrbPermissions):

    def __init__(self, isInQueue):
        super(PreQueuePermissions, self).__init__()
        self.__isInQueue = isInQueue

    def canChangeVehicle(self):
        return not self.__isInQueue

    def canCreateSquad(self):
        return not self.__isInQueue