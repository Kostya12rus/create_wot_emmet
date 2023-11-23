# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/reactive_comm/__init__.py
import adisp, wg_async
from gui.game_control.reactive_comm import Subscription, SubscriptionClientStatus, SubscriptionServerStatus
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
from web.web_client_api import w2c, w2capi, Field, W2CSchema

class _SubscriptionSchema(W2CSchema):
    channel_name = Field(required=True, type=basestring)
    get_last_message = Field(required=False, type=bool)


class _UnsubscriptionSchema(W2CSchema):
    channel_name = Field(required=True, type=basestring)


@w2capi(name='reactive_communication_service', key='action', finiHandlerName='_finiSubscriptionsHandler')
class ReactiveCommunicationWebApi(object):
    __service = dependency.descriptor(IReactiveCommunicationService)

    def __init__(self):
        super(ReactiveCommunicationWebApi, self).__init__()
        self.__subscriptions = {}

    @w2c(W2CSchema, name='is_channel_subscription_available')
    def isSubscriptionAvailable(self, _):
        return self.__service.isChannelSubscriptionAvailable

    @w2c(_SubscriptionSchema, 'subscribe_to_channel')
    def subscribe(self, cmd):
        name = cmd.channel_name.encode('utf-8')
        if name not in self.__subscriptions:
            self.__subscriptions[name] = subscription = Subscription(name)
            self.__service.onSubscriptionClosed += self.__onSubscriptionClosed
            status = yield self.__doSubscribe(subscription)
            if not status:
                self.__subscriptions.pop(name, None)
            elif cmd.get_last_message:
                self.__getLastMessage(subscription)
            yield {'channel_name': name, 
               'subscription_id': id(subscription), 
               'status': {'client': status.client.value, 
                          'server': status.server.value}}
        else:
            if cmd.get_last_message:
                self.__getLastMessage(self.__subscriptions[name])
            yield {'channel_name': name, 
               'status': {'client': SubscriptionClientStatus.AlreadySubscribed.value, 
                          'server': SubscriptionServerStatus.Subscribed.value}}
        return

    @w2c(_UnsubscriptionSchema, 'unsubscribe_from_channel')
    def unsubscribe(self, cmd):
        name = cmd.channel_name.encode('utf-8')
        success = False
        subscriptionID = 0
        if name in self.__subscriptions:
            subscription = self.__subscriptions.pop(name)
            subscriptionID = id(subscription)
            success = self.__service.unsubscribeFromChannel(subscription)
        return {'channel_name': name, 
           'subscription_id': subscriptionID, 
           'success': success}

    def _finiSubscriptionsHandler(self):
        self.__service.onSubscriptionClosed -= self.__onSubscriptionClosed
        for subscription in self.__subscriptions.values():
            self.__service.unsubscribeFromChannel(subscription)

        self.__subscriptions.clear()

    @adisp.adisp_async
    @wg_async.wg_async
    def __doSubscribe(self, subscription, callback):
        status = yield wg_async.wg_await(self.__service.subscribeToChannel(subscription))
        callback(status)

    def __getLastMessage(self, subscription):
        return self.__service.getLastMessageFromChannel(subscription)

    def __onSubscriptionClosed(self, subscription, _):
        self.__subscriptions.pop(subscription, None)
        return