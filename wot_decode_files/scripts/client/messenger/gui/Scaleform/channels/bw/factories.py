# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/channels/bw/factories.py
from messenger.gui.Scaleform.channels.bw import lobby_controllers
from messenger.gui.interfaces import IControllerFactory
from messenger.m_constants import LAZY_CHANNEL
from messenger.proto.bw import find_criteria
from messenger.storage import storage_getter

class LobbyControllersFactory(IControllerFactory):

    @storage_getter('channels')
    def channelsStorage(self):
        return

    def init(self):
        controllers = []
        channels = self.channelsStorage.getChannelsByCriteria(find_criteria.BWLobbyChannelFindCriteria())
        for channel in channels:
            controller = self.factory(channel)
            if controller is not None:
                controllers.append(controller)

        return controllers

    def factory(self, channel):
        controller = None
        if channel.getName() in LAZY_CHANNEL.ALL:
            if channel.getName() == LAZY_CHANNEL.SPECIAL_BATTLES:
                controller = lobby_controllers.BSLazyChannelController(channel)
            else:
                controller = lobby_controllers.LazyChannelController(channel)
        elif not channel.isBattle():
            controller = lobby_controllers.LobbyChannelController(channel)
        return controller