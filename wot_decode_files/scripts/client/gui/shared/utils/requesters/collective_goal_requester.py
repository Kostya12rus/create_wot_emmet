# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/collective_goal_requester.py
import logging, typing
from wg_async import wg_async, wg_await
from Event import Event
from gui.game_control.reactive_comm import Subscription
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
_logger = logging.getLogger(__name__)

class CollectiveGoalRequester(object):
    __slots__ = ('onUpdated', '__subscription', '__message')
    __reactiveCommunication = dependency.descriptor(IReactiveCommunicationService)

    def __init__(self):
        super(CollectiveGoalRequester, self).__init__()
        self.onUpdated = Event()
        self.__subscription = None
        self.__message = None
        return

    @wg_async
    def start(self, channelName):
        _logger.debug('Trying to subscribe channel: <%s>', channelName)
        if self.__subscription is not None:
            _logger.error('Requester is already subscribed to channel: <%s>', channelName)
            return
        else:
            if not self.__reactiveCommunication.isChannelSubscriptionAvailable:
                _logger.error('Channel subscription is unavailable! Please check reactive communication settings')
                return
            self.__message = None
            self.__subscription = Subscription(channelName)
            status = yield wg_await(self.__reactiveCommunication.subscribeToChannel(self.__subscription))
            _logger.debug('Subscription status for channel <%s>: %s', channelName, status)
            if status:
                self.__subscription.onClosed += self.__onClosed
                self.__subscription.onMessage += self.__onMessage
                _logger.debug('Sending get_last request for channel <%s>', channelName)
                self.__reactiveCommunication.getLastMessageFromChannel(self.__subscription)
            else:
                self.__subscription = None
            return

    def stop(self):
        if self.__subscription is not None:
            _logger.debug('Trying to unsubscribe channel: <%s>', self.__subscription.channel)
            self.__subscription.onClosed -= self.__onClosed
            self.__subscription.onMessage -= self.__onMessage
            self.__reactiveCommunication.unsubscribeFromChannel(self.__subscription)
            self.__subscription = None
        return

    def clear(self):
        self.stop()
        self.onUpdated.clear()
        self.__message = None
        return

    @property
    def isActive(self):
        return self.__subscription is not None

    def getMessage(self):
        return self.__message

    def __onMessage(self, message):
        _logger.debug('Message: %s', message)
        if message:
            self.__message = message
            self.onUpdated()

    def __onClosed(self, reason):
        _logger.debug('Subscription is closed with reason %s', reason)
        self.stop()