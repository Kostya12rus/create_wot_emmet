# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/stronghold/unit/ctx.py
from gui.prb_control import settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

class SetReserveUnitCtx(UnitRequestCtx):
    __slots__ = ('__reserveID', '__isRemove')

    def __init__(self, reserveID, waitingID='', flags=_UNDEFINED, entityType=0, isRemove=False):
        super(SetReserveUnitCtx, self).__init__(waitingID=waitingID, flags=flags, entityType=entityType)
        self.__reserveID = reserveID
        self.__isRemove = isRemove

    def getRequestType(self):
        return _REQUEST_TYPE.SET_RESERVE

    def getReserveID(self):
        return self.__reserveID

    def getIsRemove(self):
        return self.__isRemove


class UnsetReserveUnitCtx(UnitRequestCtx):
    __slots__ = ('__reserveID', '__isRemove')

    def __init__(self, reserveID, waitingID='', flags=_UNDEFINED, entityType=0, isRemove=False):
        super(UnsetReserveUnitCtx, self).__init__(waitingID=waitingID, flags=flags, entityType=entityType)
        self.__reserveID = reserveID
        self.__isRemove = isRemove

    def getRequestType(self):
        return _REQUEST_TYPE.UNSET_RESERVE

    def getReserveID(self):
        return self.__reserveID

    def getIsRemove(self):
        return self.__isRemove


class TimeoutCtx(UnitRequestCtx):
    __slots__ = ('__onTimeoutCallback', )

    def __init__(self, prbType, flags=_UNDEFINED, waitingID='', onTimeoutCallback=None):
        super(TimeoutCtx, self).__init__(entityType=prbType, waitingID=waitingID, flags=flags)
        self.__onTimeoutCallback = onTimeoutCallback

    def callTimeoutCallback(self):
        onTimeoutCallback = self.__onTimeoutCallback
        if onTimeoutCallback and callable(onTimeoutCallback):
            onTimeoutCallback()


@ReprInjector.withParent(('__rosterID', 'rosterID'))
class CreateUnitCtx(TimeoutCtx):
    __slots__ = ('__rosterID', )

    def __init__(self, prbType, flags=_UNDEFINED, waitingID='', rosterID=0, onTimeoutCallback=None):
        super(CreateUnitCtx, self).__init__(prbType=prbType, waitingID=waitingID, flags=flags, onTimeoutCallback=onTimeoutCallback)
        self.__rosterID = rosterID

    def getRequestType(self):
        return _REQUEST_TYPE.CREATE

    def getRosterID(self):
        return self.__rosterID


@ReprInjector.withParent(('__databaseID', 'databaseID'))
class GiveEquipmentCommanderCtx(UnitRequestCtx):
    __slots__ = ('__databaseID', '__role')

    def __init__(self, databaseID, role, waitingID=''):
        super(GiveEquipmentCommanderCtx, self).__init__(waitingID=waitingID)
        self.__databaseID = databaseID
        self.__role = role

    def getRequestType(self):
        return _REQUEST_TYPE.SET_EQUIPMENT_COMMANDER

    def getPlayerID(self):
        return self.__databaseID

    def getRole(self):
        return self.__role