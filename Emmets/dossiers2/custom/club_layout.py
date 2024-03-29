# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/club_layout.py
from dossiers2.common.DossierBlockBuilders import *
from battle_statistics_layouts import *
from dossiers2.custom.dependencies import CLUB_BATTLES_STAT_DEPENDENCIES
from dossiers2.custom.dependencies import CLUB_ACHIEVEMENTS_DEPENDENCIES
_rated7x7BlockBuilder = StaticSizeBlockBuilder('rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder('maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
rated7x7DossierLayout = (
 _rated7x7BlockBuilder, _maxRated7x7BlockBuilder)
_clubTotalBlockLayout = [
 'creationTime', 'lastBattleTime']
_clubTotalBlockBuilder = StaticSizeBlockBuilder('total', _clubTotalBlockLayout, {}, [])
_clubBattlesBlockLayout = [
 'battlesCount', 
 'wins', 
 'losses', 
 'killedVehicles', 
 'lostVehicles', 
 'capturePoints', 
 'droppedCapturePoints', 
 'damageDealt', 
 'damageReceived', 
 'battlesCountInAttack', 
 'damageDealtInAttack', 
 'damageDealtInDefence']
_clubBattlesBlockBuilder = StaticSizeBlockBuilder('clubBattles', _clubBattlesBlockLayout, CLUB_BATTLES_STAT_DEPENDENCIES, [])
_clubBestVehiclesBlockBuilder = DictBlockBuilder('vehicles', 'I', 'II', {})
_clubBestMapsBlockBuilder = DictBlockBuilder('maps', 'I', 'II', {})
CLUB_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'tacticalAdvantage', 'tacticalSkill', 'secretOperations', 
 'victoryMarchSeries', 
 'maxVictoryMarchSeries', 'strategicOperations']
_clubAchievementsPopUps = [
 'strategicOperations']
_clubAchievementsBlockBuilder = StaticSizeBlockBuilder('achievementsRated7x7', CLUB_ACHIEVEMENTS_BLOCK_LAYOUT, CLUB_ACHIEVEMENTS_DEPENDENCIES, _clubAchievementsPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = [
 'victoryMarch']
_singleAchievementsPopUps = ['victoryMarch']
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder('singleAchievementsRated7x7', _SINGLE_ACHIEVEMENTS_VALUES, {}, _singleAchievementsPopUps)
clubDossierLayout = (
 _clubTotalBlockBuilder, _clubBattlesBlockBuilder, _clubBestVehiclesBlockBuilder,
 _clubBestMapsBlockBuilder, _clubAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder)