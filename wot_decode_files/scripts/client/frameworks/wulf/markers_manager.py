# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/markers_manager.py
import logging, typing
from .py_object_binder import PyObjectEntity
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    import Math
_logger = logging.getLogger(__name__)

class MarkersManager(PyObjectEntity):
    __slots__ = ()

    @classmethod
    def create(cls, proxy):
        manager = MarkersManager()
        manager.bind(proxy)
        return manager

    def addMarkerStatic(self, viewModel, worldPos):
        self.proxy.addMarkerStatic(viewModel, worldPos)

    def addMarkerDynamic(self, viewModel, dataProvider):
        self.proxy.addMarkerDynamic(viewModel, dataProvider)

    def removeMarker(self, viewModel):
        self.proxy.removeMarker(viewModel)

    def clear(self):
        self.proxy.clear()

    def destroy(self):
        if self.proxy is not None:
            self.proxy.clear()
        self.unbind()
        return