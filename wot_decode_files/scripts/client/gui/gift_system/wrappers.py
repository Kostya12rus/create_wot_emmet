# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/wrappers.py
from collections import namedtuple
from functools import wraps
OpenedGiftData = namedtuple('OpenedGiftData', 'senderID, metaInfo')
GiftsHistoryData = namedtuple('GiftsHistoryData', ('aggregated', 'detailed'))
GiftsWebState = namedtuple('GiftsWebState', ('sendLimit', 'expireTime', 'expireDelta',
                                             'executionTime', 'state'))
IncomeSysMessage = namedtuple('IncomeSysMessage', ('eventID', 'senderID', 'giftItemID',
                                                   'meta', 'executionTime'))
SendGiftResponse = namedtuple('SendGiftResponse', ('state', 'receiverID', 'outCount',
                                                   'entitlementCode', 'meta', 'executionTime'))

def ifMessagesEnabled(method):

    @wraps(method)
    def wrapper(messenger, *args, **kwargs):
        if messenger.isMessagesEnabled():
            method(messenger, *args, **kwargs)

    return wrapper


def ifMessagesAllowed(msgType, useQueue=True):

    def decorator(method):

        @wraps(method)
        def wrapper(messenger, *args, **kwargs):
            if not messenger.isMessagesSuspended(*args, **kwargs):
                method(messenger, *args, **kwargs)
            elif useQueue:
                messenger.addToQueue(msgType, *args, **kwargs)

        return wrapper

    return decorator


def hasGiftEventHub(method):

    @wraps(method)
    def wrapper(hubContainer, *args, **kwargs):
        if hubContainer.getGiftEventHub() is not None:
            method(hubContainer, *args, **kwargs)
        return

    return wrapper


def skipNoHubsAction(method):

    @wraps(method)
    def wrapper(controller, hubsToAction, *args, **kwargs):
        if hubsToAction:
            method(controller, hubsToAction, *args, **kwargs)

    return wrapper


def filterGiftHubsAction(eventID):

    def decorator(method):

        @wraps(method)
        def wrapper(listener, hubsToAction, *args, **kwargs):
            if eventID in hubsToAction:
                method(listener, hubsToAction, *args, **kwargs)

        return wrapper

    return decorator