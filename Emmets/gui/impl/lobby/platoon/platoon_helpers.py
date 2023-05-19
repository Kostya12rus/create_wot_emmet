# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/platoon/platoon_helpers.py
import logging
from collections import namedtuple
from helpers import i18n
from UnitBase import BitfieldHelper
from items import vehicles
from gui.Scaleform.locale.PLATOON import PLATOON
from gui.impl.pub import WindowImpl
from frameworks.wulf import WindowFlags, WindowLayer
_logger = logging.getLogger(__name__)
Position = namedtuple('Position', ['x', 'y'])

class PreloadableWindow(WindowImpl):

    def __init__(self, wndFlags=WindowFlags.UNDEFINED, content=None, layer=WindowLayer.UNDEFINED):
        super(PreloadableWindow, self).__init__(wndFlags, content=content, layer=layer)
        self.__preload = False

    def preload(self):
        self.__preload = True
        super(PreloadableWindow, self).load()

    def _isPreloading(self):
        return self.__preload

    def _onContentReady(self):
        super(PreloadableWindow, self)._onContentReady()
        if self.__preload:
            self.__preload = False
            self.hide()

    def show(self):
        super(PreloadableWindow, self).show()
        self.bringToFront()


def removeNationFromTechName(string):
    result = string.split(':')
    if len(result) > 1:
        return result[1]
    if result:
        return result[0]
    return ''


def getNationFromTechName(string):
    result = string.split(':')
    if result:
        return result[0]
    return ''


def convertTierFilterToList(tierFilter):
    tierFilterArray = []
    unitFilter = BitfieldHelper(tierFilter)
    for bit in range(1, 11):
        if unitFilter.isSetBit(bit):
            tierFilterArray.append(bit)

    return tierFilterArray


def isExpandedTierFilter(unitFilter, tierFilterList):
    return convertTierFilterToList(unitFilter) != tierFilterList


def getVehicleDescriptorByIntCD(vehicleIntCD):
    _, nationId, itemId = vehicles.parseIntCompactDescr(vehicleIntCD)
    return vehicles.VehicleDescr(typeID=(nationId, itemId))


def getQueueInfoByQueueType(queueInfo, queueType):
    defaultQueueInfo = {'numInQueue': 0}
    if queueInfo:
        return queueInfo.get(queueType, defaultQueueInfo)
    return defaultQueueInfo


def formatSearchEstimatedTime(seconds):
    if seconds > 60 or seconds < 1:
        return i18n.makeString(PLATOON.SEARCHING_ESTIMATED_MORETHAN) % {'seconds': 60}
    if seconds <= 5:
        seconds = 5
    elif seconds <= 10:
        seconds = 10
    elif seconds <= 15:
        seconds = 15
    elif seconds <= 20:
        seconds = 20
    elif seconds <= 30:
        seconds = 30
    else:
        seconds = 60
    return i18n.makeString(PLATOON.SEARCHING_ESTIMATED_LESSTHAN) % {'seconds': seconds}