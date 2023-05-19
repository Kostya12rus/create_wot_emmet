# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/reactive_comm/__init__.py
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
from web.client_web_api.api import C2WHandler, c2w

class ReactiveCommunicationEventHandler(C2WHandler):
    __service = dependency.descriptor(IReactiveCommunicationService)

    @property
    def preventIdentical(self):
        return False

    def init(self):
        super(ReactiveCommunicationEventHandler, self).init()
        self.__service.onChannelMessage += self.__onChannelMessage
        self.__service.onSubscriptionClosed += self.__onSubscriptionClosed

    def fini(self):
        self.__service.onChannelMessage -= self.__onChannelMessage
        self.__service.onSubscriptionClosed -= self.__onSubscriptionClosed
        super(ReactiveCommunicationEventHandler, self).fini()

    @c2w(name='on_reactive_communication_channel_message')
    def __onChannelMessage(self, name, message):
        return {'channel_name': name, 
           'data': message}

    @c2w(name='on_reactive_communication_subscription_closed')
    def __onSubscriptionClosed(self, subscription, reason):
        return {'channel_name': subscription.channel, 
           'subscription_id': id(subscription), 
           'reason': reason.value}