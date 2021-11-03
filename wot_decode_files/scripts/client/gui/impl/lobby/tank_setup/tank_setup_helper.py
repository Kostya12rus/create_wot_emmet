# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/tank_setup_helper.py
import logging
from async import async, await, await_callback
from BWUtil import AsyncReturn
from gui.impl.lobby.tank_setup.tank_setup_sounds import playSlotActionSound
from items.components.supply_slot_categories import SlotCategories
_logger = logging.getLogger(__name__)
NONE_ID = -1
_CATEGORY_MASK = {category:1 << idx for idx, category in enumerate(SlotCategories.ORDER)}

def getCategoriesMask(categories):
    return sum(_CATEGORY_MASK[category] for category in categories)


def setLastSlotAction(viewModel, vehicle, setupName, actionType, intCD=NONE_ID, slotID=NONE_ID, leftID=NONE_ID, rightID=NONE_ID, leftIntCD=NONE_ID, rightIntCD=NONE_ID):
    with viewModel.lastSlotAction.transaction() as (tx):
        tx.setActionType(actionType)
        tx.setIntCD(intCD)
        tx.setInstalledSlotId(slotID)
        tx.setLeftID(leftID)
        tx.setRightID(rightID)
        tx.setLeftIntCD(leftIntCD)
        tx.setRightIntCD(rightIntCD)
    playSlotActionSound(setupName, actionType, vehicle, int(intCD), leftIntCD, rightIntCD)


def clearLastSlotAction(viewModel):
    with viewModel.lastSlotAction.transaction() as (tx):
        tx.setActionType('')
        tx.setIntCD(NONE_ID)
        tx.setInstalledSlotId(NONE_ID)
        tx.setLeftID(NONE_ID)
        tx.setRightID(NONE_ID)
        tx.setLeftIntCD(NONE_ID)
        tx.setRightIntCD(NONE_ID)


class TankSetupAsyncCommandLock(object):
    __slots__ = ('__inProcess', )

    def __init__(self):
        self.__inProcess = False

    @property
    def isLocked(self):
        return self.__inProcess

    @async
    def tryAsyncCommand(self, func, *args, **kwargs):
        if not self.__inProcess:
            try:
                self._lock()
                result = yield await(func(*args, **kwargs))
                raise AsyncReturn(result)
            finally:
                self._unlock()

        else:
            _logger.warning('Action in process')
            raise AsyncReturn(None)
        return

    @async
    def tryAsyncCommandWithCallback(self, func, *args, **kwargs):
        if not self.__inProcess:
            try:
                self._lock()
                result = yield await_callback(func)(*args, **kwargs)
                raise AsyncReturn(result)
            finally:
                self._unlock()

        else:
            _logger.debug('Action in process')
            raise AsyncReturn(None)
        return

    def _lock(self):
        self.__inProcess = True

    def _unlock(self):
        self.__inProcess = False