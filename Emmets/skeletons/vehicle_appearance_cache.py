# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/vehicle_appearance_cache.py


class IAppearanceCache(object):

    def getAppearance(self, vId, vInfo, callback=None):
        raise NotImplementedError

    def removeAppearance(self, vId):
        raise NotImplementedError

    def stopLoading(self, vId):
        raise NotImplementedError

    def loadResources(self, compactDescr, prereqs):
        raise NotImplementedError

    def unloadResources(self, compactDescr):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError