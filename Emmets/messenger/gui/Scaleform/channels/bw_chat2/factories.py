# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/channels/bw_chat2/factories.py
from constants import PREBATTLE_TYPE
from messenger.gui.gameface.channels.GFChannelController import GFChannelController
from messenger.gui.Scaleform.channels.bw_chat2 import battle_controllers
from messenger.gui.Scaleform.channels.bw_chat2 import lobby_controllers
from messenger.gui.interfaces import IControllerFactory
from messenger.m_constants import BATTLE_CHANNEL
from messenger.proto.bw_chat2 import find_criteria
from messenger.proto.bw_chat2.wrappers import CHAT_TYPE
from messenger.storage import storage_getter
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class LobbyControllersFactory(IControllerFactory):

    @storage_getter('channels')
    def channelsStorage(self):
        return

    def init(self):
        controllers = []
        channels = self.channelsStorage.getChannelsByCriteria(find_criteria.BWPrebattleChannelFindCriteria())
        for channel in channels:
            controller = self.factory(channel)
            if controller is not None:
                controllers.append(controller)

        return controllers

    def factory(self, channel):
        controller = None
        chatType = channel.getProtoData().chatType
        settings = channel.getProtoData().settings
        if chatType == CHAT_TYPE.UNIT:
            prbType = channel.getPrebattleType()
            if prbType:
                if prbType in PREBATTLE_TYPE.TRAININGS:
                    controller = lobby_controllers.TrainingChannelController(channel)
                else:
                    if settings == BATTLE_CHANNEL.SQUAD:
                        controller = GFChannelController(channel)
                    elif settings != BATTLE_CHANNEL.SQUAD:
                        controller = lobby_controllers.UnitChannelController(channel)
        return controller


class BattleControllersFactory(IControllerFactory):

    @storage_getter('channels')
    def channelsStorage(self):
        return

    def init(self):
        controllers = []
        channels = self.channelsStorage.getChannelsByCriteria(find_criteria.BWBattleChannelFindCriteria())
        for channel in channels:
            controller = self.factory(channel)
            if controller is not None:
                controllers.append(controller)

        return controllers

    def factory(self, channel):
        controller = None
        settings = channel.getProtoData().settings
        sessionProvider = dependency.instance(IBattleSessionProvider)
        arenaVisitor = sessionProvider.arenaVisitor
        if settings == BATTLE_CHANNEL.TEAM:
            if arenaVisitor.gui.isInEpicRange():
                controller = battle_controllers.EpicTeamChannelController(channel)
            else:
                controller = battle_controllers.TeamChannelController(channel)
        elif settings == BATTLE_CHANNEL.COMMON:
            controller = battle_controllers.CommonChannelController(channel)
        elif settings == BATTLE_CHANNEL.SQUAD:
            controller = battle_controllers.SquadChannelController(channel)
        return controller