# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/vehicle_appearance_cache.py


class IAppearanceCache(object):

    def getAppearance(self, vId, vInfo, callback=None, strCD=None, needLoad=True):
        raise NotImplementedError

    def removeAppearance(self, vId, strCD=None):
        raise NotImplementedError

    def stopLoading(self, vId, strCD=None):
        raise NotImplementedError

    def loadResources(self, compactDescr, prereqs):
        raise NotImplementedError

    def unloadResources(self, compactDescr):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError