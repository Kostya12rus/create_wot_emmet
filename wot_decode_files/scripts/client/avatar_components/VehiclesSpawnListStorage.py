# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/VehiclesSpawnListStorage.py
import logging, cPickle
from Event import Event
from VehiclesSpawnListStorageCommon import convertTuplesToVehicleSpawnData
_logger = logging.getLogger(__name__)

class VehiclesSpawnListStorage(object):

    def __init__(self):
        super(VehiclesSpawnListStorage, self).__init__()
        self.onSpawnListUpdated = Event()

    def handleKey(self, isDown, key, mods):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def updateSpawnList(self, spawnListData):
        spawnList = convertTuplesToVehicleSpawnData(cPickle.loads(spawnListData))
        self.onSpawnListUpdated(spawnList)