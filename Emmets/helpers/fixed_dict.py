# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/fixed_dict.py
from collections import namedtuple
import typing
RoleEquipmentState = namedtuple('RoleEquipmentState', ('level', 'progress'))
StatusWithTimeInterval = namedtuple('StatusWithTimeInterval', ('statusID', 'startTime',
                                                               'endTime'))
TimeInterval = namedtuple('TimeInterval', ('startTime', 'endTime'))
StateWithTimeInterval = namedtuple('TimeInterval', ('stateID', 'timeInterval', 'isSourceVehicle'))
VisualScriptEquipmentState = namedtuple('VisualScriptEquipmentState', ('quantity',
                                                                       'endTime',
                                                                       'totalTime',
                                                                       'prevStage',
                                                                       'stage'))
if typing.TYPE_CHECKING:
    from enum import Enum

def getRoleEquipmentState(fixedDict):
    state = RoleEquipmentState(level=fixedDict['level'], progress=fixedDict['progress'])
    return state


def getStatusWithTimeInterval(fixedDict, statusEnum=None):
    status = StatusWithTimeInterval(statusID=statusEnum(fixedDict['statusID']) if statusEnum is not None else fixedDict['statusID'], startTime=fixedDict['startTime'], endTime=fixedDict['endTime'])
    return status


def getTimeInterval(fixedDict):
    interval = TimeInterval(startTime=fixedDict['startTime'], endTime=fixedDict['endTime'])
    return interval


def getStateWithTimeInterval(fixedDict):
    state = StateWithTimeInterval(stateID=fixedDict['stateID'], timeInterval=getTimeInterval(fixedDict['timeInterval']), isSourceVehicle=fixedDict['isSourceVehicle'])
    return state


def getVisualScriptEquipmentState(fixedDict):
    state = VisualScriptEquipmentState(quantity=fixedDict['quantity'], endTime=fixedDict['endTime'], totalTime=fixedDict['totalTime'], prevStage=fixedDict['prevStage'], stage=fixedDict['stage'])
    return state