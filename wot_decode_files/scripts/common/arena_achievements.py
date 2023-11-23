# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/arena_achievements.py
from dossiers2.custom.records import RECORD_DB_IDS
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
ACHIEVEMENTS = ('warrior', 'invader', 'sniper', 'sniper2', 'mainGun', 'defender', 'steelwall',
                'supporter', 'scout', 'evileye', 'medalWittmann', 'medalOrlik', 'medalOskin',
                'medalHalonen', 'medalBurda', 'medalBillotte', 'medalKolobanov',
                'medalFadin', 'medalRadleyWalters', 'medalLafayettePool', 'medalLehvaslaiho',
                'medalNikolas', 'medalPascucci', 'medalDumitru', 'medalBrunoPietro',
                'medalTarczay', 'heroesOfRassenay', 'medalDeLanglade', 'medalTamadaYoshio',
                'raider', 'kamikaze', 'huntsman', 'bombardier', 'luckyDevil', 'ironMan',
                'sturdy', 'alaric', 'lumberjack', 'medalBrothersInArms', 'medalCrucialContribution',
                'armoredFist', 'kingOfTheHill', 'willToWinSpirit', 'shoulderToShoulder',
                'aloneInTheField', 'fallenFlags', 'effectiveSupport', 'falloutDieHard',
                'stormLord', 'winnerLaurels', 'predator', 'unreachable', 'champion',
                'bannerman', 'markIProtector', 'markIBaseProtector', 'markIBomberman',
                'markIRepairer', 'occupyingForce', 'ironShield', 'generalOfTheArmy',
                'supremeGun', 'smallArmy', 'frontlineMedal', 'se12019Medal', 'bootcampMedal',
                'se2020Medal', 'hw2019Medal', 'hw2019Medal1', 'hw2019Medal2', 'hw2019Medal3')
ACHIEVEMENTS_WITH_REWARD = set([ RECORD_DB_IDS[('achievements', name)] for name in ('warrior',
                                                                                    'invader',
                                                                                    'sniper',
                                                                                    'sniper2',
                                                                                    'mainGun',
                                                                                    'defender',
                                                                                    'steelwall',
                                                                                    'supporter',
                                                                                    'scout',
                                                                                    'evileye',
                                                                                    'heroesOfRassenay',
                                                                                    'medalFadin',
                                                                                    'medalNikolas',
                                                                                    'medalPascucci',
                                                                                    'medalLehvaslaiho',
                                                                                    'medalRadleyWalters',
                                                                                    'medalHalonen',
                                                                                    'medalDumitru',
                                                                                    'medalDeLanglade',
                                                                                    'medalOrlik',
                                                                                    'medalOskin',
                                                                                    'medalLafayettePool',
                                                                                    'medalBurda',
                                                                                    'medalTamadaYoshio',
                                                                                    'medalBrothersInArms',
                                                                                    'medalCrucialContribution',
                                                                                    'huntsman',
                                                                                    'medalStark',
                                                                                    'medalGore')
                               ] + [ RECORD_DB_IDS[('falloutAchievements', name)] for name in ('shoulderToShoulder',
                                                                                               'falloutDieHard',
                                                                                               'champion',
                                                                                               'bannerman')
                                   ])
INBATTLE_SERIES = ('sniper', 'killing', 'piercing')
INBATTLE_SERIES_INDICES = dict((x[1], x[0]) for x in enumerate(INBATTLE_SERIES))
_BILLOTTE_CMN_CNDS = {'hpPercentage': 20, 
   'minCrits': 5}
ACHIEVEMENT_CONDITIONS = {'warrior': {'minFrags': 6, 
               'minKills': 6}, 
   'invader': {'minCapturePts': 80}, 
   'sniper': {'minAccuracy': 0.85, 
              'minShots': 10, 
              'minDamage': 1000}, 
   'sniper2': {'minAccuracy': 0.85, 
               'minDamage': 1000, 
               'minHitsWithDamagePercent': 0.8, 
               'sniperDistance': 300.0, 
               'minShots': 8}, 
   'mainGun': {'minDamage': 1000, 
               'minDamageToTotalHealthRatio': 0.2}, 
   'defender': {'minPoints': 70}, 
   'steelwall': {'minDamage': 1000, 
                 'minHits': 11}, 
   'supporter': {'minAssists': 6}, 
   'scout': {'minDetections': 9}, 
   'evileye': {'minAssists': 6}, 
   'medalRadleyWalters': {'minLevel': 5, 
                          'minKills': 8, 
                          'maxKills': 9}, 
   'medalLafayettePool': {'minLevel': 5, 
                          'minKills': 10, 
                          'maxKills': 13}, 
   'heroesOfRassenay': {'minKills': 14, 
                        'maxKills': 255}, 
   'medalOrlik': {'minVictimLevelDelta': 1, 
                  'minKills': 2}, 
   'medalLehvaslaiho': {'minVictimLevelDelta': 1, 
                        'minKills': 2, 
                        'maxKills': 2}, 
   'medalOskin': {'minVictimLevelDelta': 1, 
                  'minKills': 3, 
                  'maxKills': 3}, 
   'medalNikolas': {'minVictimLevelDelta': 1, 
                    'minKills': 4, 
                    'maxKills': 255}, 
   'medalHalonen': {'minVictimLevelDelta': 2, 
                    'minKills': 2}, 
   'medalPascucci': {'minKills': 2, 
                     'maxKills': 2}, 
   'medalDumitru': {'minKills': 3, 
                    'maxKills': 255}, 
   'medalBurda': {'minVictimLevelDelta': 1, 
                  'minKills': 3, 
                  'maxKills': 255}, 
   'medalBillotte': {'cmn_cnds': _BILLOTTE_CMN_CNDS, 
                     'minKills': 2, 
                     'maxKills': 2}, 
   'medalBrunoPietro': {'cmn_cnds': _BILLOTTE_CMN_CNDS, 
                        'minKills': 3, 
                        'maxKills': 4}, 
   'medalTarczay': {'cmn_cnds': _BILLOTTE_CMN_CNDS, 
                    'minKills': 5, 
                    'maxKills': 255}, 
   'medalKolobanov': {'teamDiff': 5}, 
   'medalBrothersInArms': {'minKills': 3}, 
   'medalCrucialContribution': {'minKills': 12}, 
   'medalDeLanglade': {'minKills': 4}, 
   'medalTamadaYoshio': {'minKills': 2, 
                         'maxKills': 255, 
                         'minVictimLevelDelta': 1}, 
   'kamikaze': {'levelDelta': 1}, 
   'huntsman': {'minKills': 3}, 
   'bombardier': {'minKills': 2}, 
   'luckyDevil': {'radius': 10.99}, 
   'ironMan': {'minHits': 10}, 
   'sturdy': {'minHealth': 10.0}, 
   'alaric': {'minKills': 2, 
              'minMonuments': 1}, 
   'lumberjack': {'minKills': 3, 
                  'minTrees': 30}, 
   'wolfAmongSheep': {'minDamage': 1}, 
   'geniusForWar': {'minXP': 1}, 
   'willToWinSpirit': {'enemyCount': 3}, 
   'fightingReconnaissance': {'maxPosInTopDamager': 3, 
                              'minSpottedCount': 2}, 
   'monolith': {'maxSpeed_ms': 11 / 3.6}, 
   'medalMonolith': {'maxSpeed_ms': 11 / 3.6}, 
   'medalAntiSpgFire': {'minKills': 2}, 
   'medalStark': {'minKills': 2, 
                  'hits': 2}, 
   'medalGore': {'minDamageRate': 8, 
                 'minDamage': 2000}, 
   'medalCoolBlood': {'maxDistance': 100, 
                      'minKills': 2, 
                      'requiredVehicleLevel': 4}, 
   'promisingFighter': {'maxPosInTopXPGainer': 3}, 
   'heavyFire': {'maxPosInTopDamager': 3}, 
   'fighter': {'minKills': 4, 
               'maxKills': 5}, 
   'duelist': {'minKills': 2}, 
   'bonecrusher': {'minCrits': 5}, 
   'charmed': {'minVehs': 4}, 
   'tacticalAdvantage': {'maxLevel': 7}, 
   'secretOperations': {'minGroupLen': 2}, 
   'shoulderToShoulder': {'minKills': 12, 
                          'minDamageDealt': 30000}, 
   'aloneInTheField': {'minDamageDealt': 10000}, 
   'fallenFlags': {'minFlags': 4}, 
   'effectiveSupport': {'minDamageDealt': 2000}, 
   'falloutDieHard': {'minKills': 5, 
                      'minDamageDealt': 10000}, 
   'predator': {'minKills': 5}, 
   'champion': {'minKills': 5, 
                'minDamageDealt': 10000, 
                'minFlagsCapture': 3}, 
   'bannerman': {'minFlagsCapture': 4}, 
   'ironShield': {'minDamage': 1800, 
                  'checks': [
                           ('DestructibleEntity', 150),
                           ('SectorBase', 50)]}, 
   'occupyingForce': {'minBasePoints': 100}, 
   'supremeGun': {'minDamageDealt': 10000}, 
   'smallArmy': {'minVehiclesDestroyed': 20}, 
   'steamTopLeague': {'level': 10, 
                      'minXP': 1}, 
   'artilleryFortEquipment': {'id': range(400, 436)}}
ACHIEVEMENT_CONDITIONS_EXT = {'warrior': {'minFrags': 8, 
               'minKills': 8}, 
   'heroesOfRassenay': {'minKills': 21, 
                        'maxKills': 255}, 
   'medalLafayettePool': {'minLevel': 5, 
                          'minKills': 13, 
                          'maxKills': 20}, 
   'medalRadleyWalters': {'minLevel': 5, 
                          'minKills': 10, 
                          'maxKills': 12}}

def getAchievementCondition(arenaBonusType, medal):
    if BONUS_CAPS.checkAny(arenaBonusType, BONUS_CAPS.ACHIEVEMENT_CONDITIONS_EXT):
        if medal in ACHIEVEMENT_CONDITIONS_EXT:
            return ACHIEVEMENT_CONDITIONS_EXT[medal]
    if medal in ACHIEVEMENT_CONDITIONS:
        return ACHIEVEMENT_CONDITIONS[medal]
    return {}