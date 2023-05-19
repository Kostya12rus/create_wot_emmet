# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/ui_logger.py
from .py_object_binder import PyObjectEntity

class UILogger(PyObjectEntity):

    @classmethod
    def create(cls, proxy, model):
        manager = UILogger()
        manager.bind(proxy)
        proxy.setModel(model.proxy)
        return manager

    def getModel(self):
        return self.proxy.getModel()

    def destroy(self):
        if self.proxy is not None:
            self.proxy.clear()
        self.unbind()
        return