# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/reactive_comm/constants.py
from enum import Enum, unique
MAX_CHANNEL_HISTORY = 10
CHANNEL_UNSUBSCRIPTION_DELAY = 60

@unique
class SubscriptionCommand(Enum):
    Subscribe = 'subscribe'
    Unsubscribe = 'unsubscribe'
    GetLast = 'get_last'


@unique
class SubscriptionServerStatus(Enum):
    Subscribed = 'subscribed'
    NotExists = 'not_exists'
    ChannelsLimit = 'channels_limit'
    Unsubscribed = 'unsubscribed'
    NotSubscribed = 'not_subscribed'
    ChannelDeleted = 'channel_deleted'
    UnknownCommand = 'unknown_command'
    NameNotAllowed = 'name_not_allowed'
    CachedMessage = 'cached_message'
    NoCachedMessage = 'no_cached_message'

    @classmethod
    def fromString(cls, value):
        if value in [ item.value for item in cls ]:
            return cls(value)
        return cls.UnknownCommand


@unique
class SubscriptionClientStatus(Enum):
    NotExists = 'not_exists'
    Unsubscribed = 'unsubscribed'
    Subscribing = 'subscribing'
    Subscribed = 'subscribed'
    Unsubscribing = 'unsubscribing'
    Disabled = 'disabled'
    InvalidObject = 'invalid_object'
    NameNotAllowed = 'name_not_allowed'
    AlreadySubscribed = 'already_subscribed'


@unique
class SubscriptionCloseReason(Enum):
    Request = 'request'
    Cancel = 'cancel'
    Deleted = 'deleted'