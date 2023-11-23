# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/maps_training_appearance_cache_ctrl.py
import logging
from gui.battle_control.controllers.appearance_cache_ctrls.event_appearance_cache_ctrl import EventAppearanceCacheController
from helpers import uniprof
_logger = logging.getLogger(__name__)

class MapsTrainingAppearanceCacheController(EventAppearanceCacheController):

    @uniprof.regionDecorator(label='MapsTrainingAppearanceCacheController.updateSpawnList', scope='wrap')
    def updateSpawnList(self, spawnListData):
        self._updateSpawnList(spawnListData)
        _logger.debug('MapsTrainingAppearanceCacheController SpawnList cache updated=%s', spawnListData)