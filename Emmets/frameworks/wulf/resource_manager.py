# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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