# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/maps_training/pre_queue/ctx.py
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryIDs', 'vInvIDs'))
class MapsTrainingQueueCtx(QueueCtx):

    def __init__(self, mapGeometryID, vehCompDescr, team, waitingID=''):
        super(MapsTrainingQueueCtx, self).__init__(entityType=QUEUE_TYPE.MAPS_TRAINING, waitingID=waitingID)
        self.__mapGeometryID = mapGeometryID
        self.__vehCompDescr = vehCompDescr
        self.__team = team

    def getSelectedMap(self):
        return self.__mapGeometryID

    def getSelectedVehicle(self):
        return self.__vehCompDescr

    def getSelectedTeam(self):
        return self.__team