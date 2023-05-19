# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiCaptureBlockerComponent.py
import logging, typing
from PoiBaseComponent import PoiBaseComponent
from helpers import fixed_dict
from points_of_interest.components import PoiCaptureBlockerStateComponent
from points_of_interest_shared import PoiBlockReasons
_logger = logging.getLogger(__name__)

class PoiCaptureBlockerComponent(PoiBaseComponent):

    def __init__(self):
        super(PoiCaptureBlockerComponent, self).__init__()
        self.__stateComponent = None
        return

    def onDestroy(self):
        self._poiGameObject.removeComponent(self.__stateComponent)
        self.__stateComponent = None
        super(PoiCaptureBlockerComponent, self).onDestroy()
        return

    def set_blockReasons(self, prev):
        if self.__stateComponent is not None:
            self.__stateComponent.blockReasons = self.__getBlockReasons()
        return

    def _onAvatarReady(self):
        if self._poiGameObject is None:
            _logger.warning('PoiGameObject is not valid! Could not create PoiCaptureBlockerStateComponent')
            return
        else:
            blockReasons = self.__getBlockReasons()
            self.__stateComponent = self._poiGameObject.createComponent(PoiCaptureBlockerStateComponent, self.pointID, blockReasons)
            return

    def __getBlockReasons(self):
        return tuple(fixed_dict.getStatusWithTimeInterval(reason, PoiBlockReasons) for reason in self.blockReasons)