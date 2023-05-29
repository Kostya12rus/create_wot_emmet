# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/tankman_layout.py
from dossiers2.common.DossierBlockBuilders import *
_tmanTotalBlockLayout = [
 'battlesCount']
_tmanTotalBlockBuilder = StaticSizeBlockBuilder('total', _tmanTotalBlockLayout, {}, [])
TMAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'warrior', 
 'invader', 
 'sniper', 
 'defender', 
 'steelwall', 
 'supporter', 
 'scout', 
 'evileye', 
 'medalWittmann', 
 'medalOrlik', 
 'medalOskin', 
 'medalHalonen', 
 'medalBurda', 
 'medalBillotte', 
 'medalKolobanov', 
 'medalFadin', 
 'medalRadleyWalters', 
 'medalBrunoPietro', 
 'medalTarczay', 
 'medalPascucci', 
 'medalDumitru', 
 'medalLehvaslaiho', 
 'medalNikolas', 
 'medalLafayettePool', 
 'heroesOfRassenay', 
 'medalDeLanglade', 
 'medalTamadaYoshio', 
 'huntsman', 
 'sniper2', 
 'mainGun']
_tankmanAchievementsBlockBuilder = StaticSizeBlockBuilder('achievements', TMAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, [])
tmanDossierLayout = (
 _tmanTotalBlockBuilder,
 _tankmanAchievementsBlockBuilder)