# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/tutorial.py
import logging, typing
from .py_object_binder import PyObjectEntity
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
_logger = logging.getLogger(__name__)

class Tutorial(PyObjectEntity):
    __slots__ = ()

    @classmethod
    def create(cls, proxy, model):
        manager = Tutorial()
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