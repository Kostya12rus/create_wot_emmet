# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/resource_manager.py
import typing
from .py_object_binder import PyObjectEntity

class ResourceManager(PyObjectEntity):

    @classmethod
    def create(cls, proxy):
        manager = ResourceManager()
        manager.bind(proxy)
        return manager

    def destroy(self):
        self.unbind()

    def getTranslatedText(self, resourceID):
        return self.proxy.getTranslatedText(resourceID)

    def getImagePath(self, resourceID):
        return self.proxy.getImagePath(resourceID)

    def getSoundEffectId(self, resourceID):
        return self.proxy.getSoundEffectId(resourceID)