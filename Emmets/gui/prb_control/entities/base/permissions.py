# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/permissions.py


class IPrbPermissions(object):

    def canExitFromQueue(self):
        return True

    def canChangeVehicle(self):
        return True

    def canSendInvite(self):
        return False

    def canCreateSquad(self):
        return False