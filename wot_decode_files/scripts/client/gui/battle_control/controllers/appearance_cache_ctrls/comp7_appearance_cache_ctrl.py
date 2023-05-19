# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/comp7_appearance_cache_ctrl.py
import logging
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController
_logger = logging.getLogger(__name__)

class Comp7AppearanceCacheController(DefaultAppearanceCacheController):

    def __init__(self, setup):
        super(Comp7AppearanceCacheController, self).__init__(setup)
        self.__pendingReloads = {}

    def stopControl(self):
        self.__pendingReloads.clear()
        super(Comp7AppearanceCacheController, self).stopControl()

    def arenaLoadCompleted(self):
        super(Comp7AppearanceCacheController, self).arenaLoadCompleted()
        for vId, args in self.__pendingReloads.iteritems():
            self.reloadAppearance(vId, *args)

        self.__pendingReloads.clear()

    def reloadAppearance(self, vId, vInfo, callback=None, strCD=None, oldStrCD=None):
        if not self._spaceLoaded:
            self.__pendingReloads[vId] = (
             vInfo, callback, strCD)
            _logger.info('Appearance reload was suspended. vId=%s; vInfo=%s', vId, vInfo._asdict())
            return None
        else:
            return super(Comp7AppearanceCacheController, self).reloadAppearance(vId, vInfo, callback, strCD, oldStrCD)