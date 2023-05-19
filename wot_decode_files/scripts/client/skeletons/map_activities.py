# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/map_activities.py


class IMapActivities(object):
    __slots__ = ()

    def start(self, name, targetTime):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def generateOfflineActivities(self, spacePath, usePossibility=True):
        raise NotImplementedError