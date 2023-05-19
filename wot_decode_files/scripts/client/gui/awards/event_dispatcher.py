# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/awards/event_dispatcher.py
import gui.awards.special_achievement_awards as specialAwards
from gui.shared.event_dispatcher import showAwardWindow
from gui.impl.lobby.reward_window import DynamicRewardWindow

def showResearchAward(vehiclesCount, messageNumber):
    showAwardWindow(specialAwards.ResearchAward(vehiclesCount, messageNumber))


def showVictoryAward(victoriesCount, messageNumber):
    showAwardWindow(specialAwards.VictoryAward(victoriesCount, messageNumber))


def showBattleAward(battlesCount, messageNumber):
    showAwardWindow(specialAwards.BattleAward(battlesCount, messageNumber))


def showBoosterAward(booster):
    showAwardWindow(specialAwards.BoosterAward(booster))


def showClanJoinAward(clanAbbrev, clanName, clanDbID):
    showAwardWindow(specialAwards.ClanJoinAward(clanAbbrev, clanName, clanDbID))


def showTelecomAward(vehicleDesrs, bundleID, hasCrew, hasBrotherhood):
    showAwardWindow(specialAwards.TelecomAward(vehicleDesrs, bundleID, hasCrew, hasBrotherhood))


def showRecruiterAward():
    showAwardWindow(specialAwards.RecruiterAward())


def showDynamicAward(eventName, bonuses):
    window = DynamicRewardWindow({'eventName': eventName, 'bonuses': bonuses})
    window.load()


def showVehicleCollectorAward(nationID):
    showAwardWindow(specialAwards.VehicleCollectorAward(nationID))


def showVehicleCollectorOfEverythingAward(*args):
    showAwardWindow(specialAwards.VehicleCollectorOfEverythingAward())