# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/maps_training_common/maps_training_constants.py
MT_PDATA_KEY = 'mapsTraining'
DEFAULT_PROGRESS_VALUE = 0
MAP_PROGRESS_COMPLETE = 15
MAX_SCENARIO_PROGRESS = 1
VEHICLE_CLASSES_ORDER = ('heavyTank', 'mediumTank', 'lightTank', 'AT-SPG', 'SPG')
PROGRESS_DATA_MASK = 1

class SCENARIO_RESULT:
    LOSE = -1
    PARTIAL = 0
    WIN = 1


class VEHICLE_TYPE:
    HEAVY = 'heavyTank'
    MEDIUM = 'mediumTank'
    ALL_TYPES = [
     HEAVY, MEDIUM]
    TEAM1 = 1
    TEAM2 = 2
    ALL_TEAMS = [
     TEAM1, TEAM2]
    OFFSET = {TEAM1: {HEAVY: 0, 
               MEDIUM: 1}, 
       TEAM2: {HEAVY: 2, 
               MEDIUM: 3}}


SCENARIO_ORDER = [
 (
  VEHICLE_TYPE.TEAM1, VEHICLE_TYPE.HEAVY),
 (
  VEHICLE_TYPE.TEAM2, VEHICLE_TYPE.HEAVY),
 (
  VEHICLE_TYPE.TEAM1, VEHICLE_TYPE.MEDIUM),
 (
  VEHICLE_TYPE.TEAM2, VEHICLE_TYPE.MEDIUM)]
SCENARIO_INDEXES = {key: i + 1 for i, key in enumerate(SCENARIO_ORDER)}