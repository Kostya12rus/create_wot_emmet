# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/battleground/airdrops.py
from constants import AirdropType
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from arena_component_system.client_arena_component_system import ClientArenaComponent
from battleground.bot_drop_object import BotAirdrop
from battleground.loot_drop_object import PlaneLootAirdrop

class Airdrops(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def scheduleLoot(self, dropID, position, serverTime):
        planeObj = PlaneLootAirdrop(dropID, position, serverTime)
        planeObj.start()

    def scheduleBot(self, dropID, position, teamID, yawAxis, serverTime, airdropType=AirdropType.BOT):
        botObj = BotAirdrop(dropID, position, teamID, yawAxis, serverTime, airdropType)
        botObj.start()


class AirdropsComponent(ClientArenaComponent, Airdrops):

    def __init__(self, componentSystem):
        Airdrops.__init__(self)
        ClientArenaComponent.__init__(self, componentSystem)