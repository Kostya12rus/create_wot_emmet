# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/comp7_i18n_helpers.py
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.division_tooltip_model import Rank, Division
RANK_MAP = {Rank.FIRST: 'first', 
   Rank.SECOND: 'second', 
   Rank.THIRD: 'third', 
   Rank.FOURTH: 'fourth', 
   Rank.FIFTH: 'fifth', 
   Rank.SIXTH: 'sixth'}
DIVISION_MAP = {Division.A: 'A', 
   Division.B: 'B', 
   Division.C: 'C', 
   Division.D: 'D', 
   Division.E: 'E'}

def getRankLocale(rank):
    rankString = RANK_MAP[Rank(rank)]
    return backport.text(R.strings.comp7.rank.dyn(rankString)())


def getDivisionLocale(division):
    divisionString = DIVISION_MAP[Division(division)]
    return backport.text(R.strings.comp7.division.dyn(divisionString)())