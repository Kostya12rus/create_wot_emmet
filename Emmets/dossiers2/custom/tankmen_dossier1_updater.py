# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/tankmen_dossier1_updater.py
import dossiers2, struct
__TANKMAN_LAYOUT_10 = [
 '_version', 
 'lastBattleTime', 'battleLifeTime', 'maxFrags', 
 'xp', 'maxXP', 
 'battlesCount', 'wins', 'losses', 'survivedBattles', 'winAndSurvived', 
 'frags', 
 'frags8p', 'fragsBeast', 'shots', 'directHits', 'spotted', 'damageDealt', 
 'damageReceived', 
 'treesCut', 'capturePoints', 'droppedCapturePoints', 'sniperSeries', 
 'maxSniperSeries', 
 'invincibleSeries', 'maxInvincibleSeries', 'diehardSeries', 
 'maxDiehardSeries', 
 'killingSeries', 'maxKillingSeries', 'piercingSeries', 
 'maxPiercingSeries', 
 'battleHeroes', 
 'warrior', 'invader', 'sniper', 'defender', 'steelwall', 
 'supporter', 'scout', 
 'medalKay', 'medalCarius', 'medalKnispel', 'medalPoppel', 
 'medalAbrams', 'medalLeClerc', 
 'medalLavrinenko', 'medalEkins', 'medalWittmann', 
 'medalOrlik', 'medalOskin', 'medalHalonen', 
 'medalBurda', 'medalBillotte', 
 'medalKolobanov', 'medalFadin', 
 'beasthunter', 'titleSniper', 'invincible', 
 'diehard', 'raider', 
 'handOfDeath', 'armorPiercer', 'kamikaze', 'lumberjack']
__TANKMAN_LAYOUT_11 = [
 '_version', 
 'battlesCount', 
 'warrior', 'invader', 'sniper', 'defender', 
 'steelwall', 'supporter', 'scout', 'evileye', 
 'medalWittmann', 'medalOrlik', 
 'medalOskin', 'medalHalonen', 
 'medalBurda', 'medalBillotte', 'medalKolobanov', 
 'medalFadin', 
 'medalHeroesOfRassenai', 'medalDeLaglanda', 'medalTamadaYoshio', 
 'medalErohin', 
 'medalHoroshilov', 'medalLister']
__TANKMAN_LAYOUT_12 = [
 '_version', 
 'battlesCount', 
 'warrior', 'invader', 'sniper', 'defender', 
 'steelwall', 'supporter', 'scout', 'evileye', 
 'medalWittmann', 'medalOrlik', 
 'medalOskin', 'medalHalonen', 
 'medalBurda', 'medalBillotte', 'medalKolobanov', 
 'medalFadin', 'medalRadleyWalters', 
 'medalBrunoPietro', 'medalTarczay', 
 'medalPascucci', 'medalDumitru', 'medalLehvaslaiho', 
 'medalNikolas', 'medalLafayettePool']
__TANKMAN_LAYOUT_13 = [
 '_version', 
 'battlesCount', 
 'warrior', 'invader', 'sniper', 'defender', 
 'steelwall', 'supporter', 'scout', 'evileye', 
 'medalWittmann', 'medalOrlik', 
 'medalOskin', 'medalHalonen', 
 'medalBurda', 'medalBillotte', 'medalKolobanov', 
 'medalFadin', 'medalRadleyWalters', 
 'medalBrunoPietro', 'medalTarczay', 
 'medalPascucci', 'medalDumitru', 'medalLehvaslaiho', 
 'medalNikolas', 'medalLafayettePool', 
 'heroesOfRassenay']
__TANKMAN_LAYOUT_14 = [
 '_version', 
 'battlesCount', 
 'warrior', 'invader', 'sniper', 'defender', 
 'steelwall', 'supporter', 'scout', 'evileye', 
 'medalWittmann', 'medalOrlik', 
 'medalOskin', 'medalHalonen', 
 'medalBurda', 'medalBillotte', 'medalKolobanov', 
 'medalFadin', 'medalRadleyWalters', 
 'medalBrunoPietro', 'medalTarczay', 
 'medalPascucci', 'medalDumitru', 'medalLehvaslaiho', 
 'medalNikolas', 'medalLafayettePool', 
 'heroesOfRassenay', 'medalDeLanglade', 
 'medalTamadaYoshio']
__RECORD_PACKING_10 = {'spotted': ('I', 4, 4000000001), 
   'medalCarius': ('B', 1, 4), 
   'medalHalonen': ('B', 1, 201), 
   'invader': ('H', 2, 60001), 
   'medalFadin': ('B', 1, 201), 
   'armorPiercer': ('B', 1, 1), 
   'damageReceived': ('I', 4, 4000000001), 
   'sniperSeries': ('H', 2, 60001), 
   'battleLifeTime': ('I', 4, 4000000001), 
   'battleHeroes': ('H', 2, 60001), 
   'medalOskin': ('B', 1, 201), 
   'droppedCapturePoints': ('I', 4, 4000000001), 
   'defender': ('H', 2, 60001), 
   'xp': ('I', 4, 4000000001), 
   'medalLeClerc': ('B', 1, 4), 
   'invincibleSeries': ('B', 1, 201), 
   'supporter': ('H', 2, 60001), 
   'maxInvincibleSeries': ('B', 1, 201), 
   'steelwall': ('H', 2, 60001), 
   'medalAbrams': ('B', 1, 4), 
   'maxFrags': ('B', 1, 201), 
   'fragsBeast': ('I', 4, 4000000001), 
   'maxDiehardSeries': ('B', 1, 201), 
   'winAndSurvived': ('I', 4, 4000000001), 
   'killingSeries': ('B', 1, 201), 
   'lastBattleTime': ('I', 4, 4000000001), 
   'piercingSeries': ('B', 1, 201), 
   'diehard': ('B', 1, 1), 
   'maxSniperSeries': ('H', 2, 60001), 
   'medalKay': ('B', 1, 4), 
   'medalEkins': ('B', 1, 4), 
   'handOfDeath': ('B', 1, 1), 
   'frags': ('I', 4, 4000000001), 
   'sniper': ('H', 2, 60001), 
   'medalPoppel': ('B', 1, 4), 
   'warrior': ('H', 2, 60001), 
   'titleSniper': ('B', 1, 1), 
   'treesCut': ('H', 2, 60001), 
   'maxXP': ('H', 2, 60001), 
   'medalWittmann': ('B', 1, 201), 
   'survivedBattles': ('I', 4, 4000000001), 
   'medalBurda': ('B', 1, 201), 
   'maxPiercingSeries': ('B', 1, 201), 
   'battlesCount': ('I', 4, 4000000001), 
   'scout': ('H', 2, 60001), 
   'beasthunter': ('B', 1, 1), 
   'kamikaze': ('B', 1, 201), 
   'raider': ('B', 1, 201), 
   'diehardSeries': ('B', 1, 201), 
   'medalBillotte': ('B', 1, 201), 
   'medalLavrinenko': ('B', 1, 4), 
   'medalKolobanov': ('B', 1, 201), 
   'wins': ('I', 4, 4000000001), 
   'lumberjack': ('B', 1, 1), 
   'losses': ('I', 4, 4000000001), 
   'damageDealt': ('I', 4, 4000000001), 
   '_version': ('H', 2, 32767), 
   'medalKnispel': ('B', 1, 4), 
   'medalOrlik': ('B', 1, 201), 
   'maxKillingSeries': ('B', 1, 201), 
   'shots': ('I', 4, 4000000001), 
   'invincible': ('B', 1, 1), 
   'frags8p': ('I', 4, 4000000001), 
   'capturePoints': ('I', 4, 4000000001), 
   'directHits': ('I', 4, 4000000001)}
__RECORD_PACKING_11 = {'medalFadin': ('H', 2, 60001), 
   'defender': ('H', 2, 60001), 
   'supporter': ('H', 2, 60001), 
   'sniper': ('H', 2, 60001), 
   'medalHoroshilov': ('H', 2, 60001), 
   'scout': ('H', 2, 60001), 
   'medalKolobanov': ('H', 2, 60001), 
   'invader': ('H', 2, 60001), 
   'warrior': ('H', 2, 60001), 
   'medalWittmann': ('H', 2, 60001), 
   'medalBillotte': ('H', 2, 60001), 
   '_version': ('H', 2, 32767), 
   'evileye': ('H', 2, 60001), 
   'medalHalonen': ('H', 2, 60001), 
   'steelwall': ('H', 2, 60001), 
   'medalDeLaglanda': ('H', 2, 60001), 
   'battlesCount': ('I', 4, 4000000001), 
   'medalOskin': ('H', 2, 60001), 
   'medalTamadaYoshio': ('H', 2, 60001), 
   'medalErohin': ('H', 2, 60001), 
   'medalOrlik': ('H', 2, 60001), 
   'medalBurda': ('H', 2, 60001), 
   'medalLister': ('H', 2, 60001), 
   'medalHeroesOfRassenai': ('H', 2, 60001)}
__RECORD_PACKING_12 = {'medalFadin': ('H', 2, 60001), 
   'defender': ('H', 2, 60001), 
   'supporter': ('H', 2, 60001), 
   'medalLehvaslaiho': ('H', 2, 60001), 
   'medalPascucci': ('H', 2, 60001), 
   'sniper': ('H', 2, 60001), 
   'scout': ('H', 2, 60001), 
   'medalKolobanov': ('H', 2, 60001), 
   'medalLafayettePool': ('H', 2, 60001), 
   'invader': ('H', 2, 60001), 
   'warrior': ('H', 2, 60001), 
   'medalWittmann': ('H', 2, 60001), 
   'medalRadleyWalters': ('H', 2, 60001), 
   'medalBillotte': ('H', 2, 60001), 
   '_version': ('H', 2, 32767), 
   'evileye': ('H', 2, 60001), 
   'medalHalonen': ('H', 2, 60001), 
   'steelwall': ('H', 2, 60001), 
   'medalTarczay': ('H', 2, 60001), 
   'battlesCount': ('I', 4, 4000000001), 
   'medalOskin': ('H', 2, 60001), 
   'medalDumitru': ('H', 2, 60001), 
   'medalBrunoPietro': ('H', 2, 60001), 
   'medalOrlik': ('H', 2, 60001), 
   'medalBurda': ('H', 2, 60001), 
   'medalNikolas': ('H', 2, 60001)}
__RECORD_PACKING_13 = {'medalFadin': ('H', 2, 60001), 
   'heroesOfRassenay': ('H', 2, 60001), 
   'defender': ('H', 2, 60001), 
   'supporter': ('H', 2, 60001), 
   'medalLehvaslaiho': ('H', 2, 60001), 
   'medalPascucci': ('H', 2, 60001), 
   'sniper': ('H', 2, 60001), 
   'scout': ('H', 2, 60001), 
   'medalKolobanov': ('H', 2, 60001), 
   'medalLafayettePool': ('H', 2, 60001), 
   'invader': ('H', 2, 60001), 
   'warrior': ('H', 2, 60001), 
   'medalWittmann': ('H', 2, 60001), 
   'medalRadleyWalters': ('H', 2, 60001), 
   'medalBillotte': ('H', 2, 60001), 
   '_version': ('H', 2, 32767), 
   'evileye': ('H', 2, 60001), 
   'medalHalonen': ('H', 2, 60001), 
   'steelwall': ('H', 2, 60001), 
   'medalTarczay': ('H', 2, 60001), 
   'battlesCount': ('I', 4, 4000000001), 
   'medalOskin': ('H', 2, 60001), 
   'medalDumitru': ('H', 2, 60001), 
   'medalBrunoPietro': ('H', 2, 60001), 
   'medalOrlik': ('H', 2, 60001), 
   'medalBurda': ('H', 2, 60001), 
   'medalNikolas': ('H', 2, 60001)}
__RECORD_PACKING_14 = {'medalHalonen': ('H', 2, 60001), 
   'medalFadin': ('H', 2, 60001), 
   'heroesOfRassenay': ('H', 2, 60001), 
   'defender': ('H', 2, 60001), 
   'supporter': ('H', 2, 60001), 
   'steelwall': ('H', 2, 60001), 
   'medalLehvaslaiho': ('H', 2, 60001), 
   'medalPascucci': ('H', 2, 60001), 
   'medalTarczay': ('H', 2, 60001), 
   'sniper': ('H', 2, 60001), 
   'battlesCount': ('I', 4, 4000000001), 
   'scout': ('H', 2, 60001), 
   'medalOskin': ('H', 2, 60001), 
   'medalKolobanov': ('H', 2, 60001), 
   'medalLafayettePool': ('H', 2, 60001), 
   'medalOrlik': ('H', 2, 60001), 
   'medalDumitru': ('H', 2, 60001), 
   'invader': ('H', 2, 60001), 
   'medalBrunoPietro': ('H', 2, 60001), 
   'medalRadleyWalters': ('H', 2, 60001), 
   'medalDeLanglade': ('H', 2, 60001), 
   'medalTamadaYoshio': ('H', 2, 60001), 
   'warrior': ('H', 2, 60001), 
   'medalWittmann': ('H', 2, 60001), 
   'medalBurda': ('H', 2, 60001), 
   'medalNikolas': ('H', 2, 60001), 
   'medalBillotte': ('H', 2, 60001), 
   '_version': ('H', 2, 32767), 
   'evileye': ('H', 2, 60001)}

def __getVersion(compDescr):
    return struct.unpack('<H', compDescr[0:2])[0]


def __buildRecordsFmt(recordsLayout, recordPackings):
    fmt = '<'
    for record in recordsLayout:
        packing = recordPackings[record]
        fmt += packing[0]

    return fmt


def updateDossierCompDescr(compDescr):
    data = {}
    verDescr = __getVersion(compDescr)
    recordsLayout = __TANKMAN_LAYOUT_14
    record_packing = __RECORD_PACKING_14
    if verDescr == 10:
        recordsLayout = __TANKMAN_LAYOUT_10
        record_packing = __RECORD_PACKING_10
    else:
        if verDescr == 11:
            recordsLayout = __TANKMAN_LAYOUT_11
            record_packing = __RECORD_PACKING_11
        else:
            if verDescr == 12:
                recordsLayout = __TANKMAN_LAYOUT_12
                record_packing = __RECORD_PACKING_12
            elif verDescr == 13:
                recordsLayout = __TANKMAN_LAYOUT_13
                record_packing = __RECORD_PACKING_13
            fmt = __buildRecordsFmt(recordsLayout, record_packing)
            values = struct.unpack(fmt, compDescr)
            for index, record in enumerate(recordsLayout):
                data[record] = values[index]

        d2 = dossiers2.getTankmanDossierDescr()
        total = d2.expand('total')
        total.eventsEnabled = False
        total['battlesCount'] = data['battlesCount']
        achievements = d2.expand('achievements')
        achievements.eventsEnabled = False
        for record in ['warrior', 'invader', 'sniper', 'defender', 'steelwall', 'supporter', 
         'scout', 
         'evileye', 'medalWittmann', 'medalOrlik', 
         'medalOskin', 'medalHalonen', 'medalBurda', 
         'medalBillotte', 
         'medalKolobanov', 'medalFadin', 'medalRadleyWalters', 
         'medalBrunoPietro', 
         'medalTarczay', 'medalPascucci', 'medalDumitru', 'medalLehvaslaiho', 
         'medalNikolas', 
         'medalLafayettePool', 'heroesOfRassenay', 'medalDeLanglade', 
         'medalTamadaYoshio']:
            achievements[record] = data.get(record, 0)

    return d2.makeCompDescr()