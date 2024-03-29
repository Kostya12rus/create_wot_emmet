# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/notification/BaseNotificationView.py
from debug_utils import LOG_ERROR
_NOT_ID_TUPLE_INDEX = 2

class BaseNotificationView(object):

    def __init__(self, model=None):
        super(BaseNotificationView, self).__init__()
        self._model = None
        self.__flashIDCounter = 0
        self.__flashIdToEntityIdMap = {}
        self.__entityIdToFlashIdMap = {}
        self.setModel(model)
        return

    def setModel(self, value):
        self._model = value

    def cleanUp(self):
        self._model = None
        return

    def _getFlashID(self, notificationInfo):
        if notificationInfo in self.__entityIdToFlashIdMap:
            return self.__entityIdToFlashIdMap[notificationInfo]
        self.__flashIDCounter += 1
        self.__flashIdToEntityIdMap[self.__flashIDCounter] = notificationInfo
        self.__entityIdToFlashIdMap[notificationInfo] = self.__flashIDCounter
        return self.__flashIDCounter

    def _getNotificationID(self, flashId):
        if flashId in self.__flashIdToEntityIdMap:
            return self.__flashIdToEntityIdMap[flashId][_NOT_ID_TUPLE_INDEX]
        LOG_ERROR('Wrong notification ScaleForm id', flashId)