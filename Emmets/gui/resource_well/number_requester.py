# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/resource_well/number_requester.py
import json, logging, typing, async
from Event import Event
from gui.game_control.reactive_comm import Subscription
from gui.resource_well.resource_well_helpers import getNumberChannelName
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from typing import Optional

class ResourceWellNumberRequester(object):
    __slots__ = ('onUpdated', '__isSerial', '__subscription', '__remainingValues',
                 '__givenValues', '__isActive')
    __reactiveCommunication = dependency.descriptor(IReactiveCommunicationService)

    def __init__(self, isSerial):
        super(ResourceWellNumberRequester, self).__init__()
        self.onUpdated = Event()
        self.__isSerial = isSerial
        self.__subscription = None
        self.__remainingValues = None
        self.__givenValues = None
        self.__isActive = False
        return

    def start(self):
        self.__isActive = True
        self.__subscribe()

    def stop(self):
        if self.__isActive:
            self.__unsubscribe()
        self.__isActive = False

    def clear(self):
        self.onUpdated.clear()
        self.__subscription = None
        self.__remainingValues = None
        self.__givenValues = None
        self.__isActive = False
        return

    def getRemainingValues(self):
        return self.__remainingValues

    def getGivenValues(self):
        return self.__givenValues

    def isDataAvailable(self):
        return self.__remainingValues is not None and self.__givenValues is not None

    @async.async
    def __subscribe(self):
        channelName = self.__getChannelName()
        _logger.debug('Trying to subscribe channel: <%s>', channelName)
        if self.__subscription is not None:
            _logger.debug('Requester is already subscribed to channel: <%s>', channelName)
            return
        else:
            if not self.__reactiveCommunication.isChannelSubscriptionAvailable:
                _logger.error('Channel subscription is unavailable! Please check reactive communication settings')
                return
            self.__subscription = Subscription(channelName)
            status = yield async.await(self.__reactiveCommunication.subscribeToChannel(self.__subscription))
            _logger.debug('Subscription status for channel <%s>: %s', channelName, status)
            if status:
                self.__subscription.onClosed += self.__onClosed
                self.__subscription.onMessage += self.__onMessage
                _logger.debug('Sending get_last request for channel <%s>', channelName)
                self.__reactiveCommunication.getLastMessageFromChannel(self.__subscription)
            else:
                self.__unsubscribe()
            return

    def __unsubscribe(self):
        if self.__subscription is not None:
            _logger.debug('Trying to unsubscribe channel: <%s>', self.__subscription.channel)
            self.__subscription.onClosed -= self.__onClosed
            self.__subscription.onMessage -= self.__onMessage
            self.__reactiveCommunication.unsubscribeFromChannel(self.__subscription)
            self.__subscription = None
        return

    def __onMessage(self, message):
        _logger.debug('Message: %s', message)
        if message:
            message = json.loads(message)
            message = {str(k):v for k, v in message.iteritems()}
            remainingValues = message.get('remaining_values')
            givenValues = message.get('given_values')
        else:
            remainingValues = None
            givenValues = None
        self.__remainingValues = remainingValues
        self.__givenValues = givenValues
        if self.__remainingValues is None:
            _logger.warning('Remaining values for resource well is None!')
        if self.__givenValues is None:
            _logger.warning('Given values for resource well is None!')
        self.onUpdated()
        return

    def __onClosed(self, *_):
        self.__unsubscribe()

    def __getChannelName(self):
        return getNumberChannelName(isSerial=self.__isSerial)