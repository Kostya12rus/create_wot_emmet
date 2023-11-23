# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/script_component/DynamicScriptComponent.py
import logging, BigWorld
from PlayerEvents import g_playerEvents
from shared_utils import nextTick
_logger = logging.getLogger(__name__)

class DynamicScriptComponent(BigWorld.DynamicScriptComponent):

    def __init__(self, *_, **__):
        BigWorld.DynamicScriptComponent.__init__(self)
        if self._isAvatarReady:
            nextTick(self._onAvatarReady)()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        _logger.debug('%s.__init__. EntityID=%s', self.__class__.__name__, self.entity.id)

    @property
    def _isAvatarReady(self):
        return BigWorld.player().userSeesWorld()

    def onDestroy(self):
        _logger.debug('%s.onDestroy. EntityID=%s', self.__class__.__name__, self.entity.id)
        g_playerEvents.onAvatarReady -= self.__onAvatarReady

    def onLeaveWorld(self):
        self.onDestroy()

    @property
    def spaceID(self):
        return self.entity.spaceID

    @property
    def keyName(self):
        return next(name for name, value in self.entity.dynamicComponents.iteritems() if value == self)

    def _onAvatarReady(self):
        pass

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        self._onAvatarReady()