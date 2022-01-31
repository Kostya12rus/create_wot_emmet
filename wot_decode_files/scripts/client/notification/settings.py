# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/notification/settings.py
LIST_SCROLL_STEP_FACTOR = 10
DEF_ICON_PATH = '../maps/icons/library/{0:>s}-1.png'

class NOTIFICATION_STATE(object):
    POPUPS = 0
    LIST = 1


class NOTIFICATION_TYPE(object):
    UNDEFINED = 0
    MESSAGE = 1
    INVITE = 2
    FRIENDSHIP_RQ = 3
    WGNC_POP_UP = 4
    CLAN_INVITES = 5
    CLAN_APPS = 6
    CLAN_APP_ACTION = 7
    CLAN_INVITE_ACTION = 8
    CLAN_INVITE = 9
    CLAN_APP = 10
    PROGRESSIVE_REWARD = 11
    MISSING_EVENTS = 12
    CHOOSING_DEVICES = 13
    RECRUIT_REMINDER = 14
    EMAIL_CONFIRMATION_REMINDER = 15
    PSACOIN_REMINDER = 16
    GIFT_SYSTEM_OPERATION = 17
    NEW_YEAR_SPECIAL_LOOTBOXES = 18
    LUNAR_NY_ENVELOPES_RECEIVED = 19
    LUNAR_NY_NEW_ENVELOPES_RECEIVED = 20
    LUNAR_NY_NEW_ENVELOPES_RECEIVED_SIMPLE = 21
    RANGE = (
     MESSAGE, INVITE, FRIENDSHIP_RQ, WGNC_POP_UP, CLAN_INVITES, CLAN_APPS, CLAN_APP_ACTION, CLAN_INVITE_ACTION,
     CLAN_INVITE, CLAN_APP, PROGRESSIVE_REWARD, MISSING_EVENTS, CHOOSING_DEVICES, RECRUIT_REMINDER,
     EMAIL_CONFIRMATION_REMINDER, LUNAR_NY_ENVELOPES_RECEIVED, LUNAR_NY_NEW_ENVELOPES_RECEIVED,
     LUNAR_NY_NEW_ENVELOPES_RECEIVED_SIMPLE, PSACOIN_REMINDER, GIFT_SYSTEM_OPERATION, NEW_YEAR_SPECIAL_LOOTBOXES)


ITEMS_MAX_LENGTHS = {NOTIFICATION_TYPE.MESSAGE: 250, 
   NOTIFICATION_TYPE.INVITE: 100, 
   NOTIFICATION_TYPE.FRIENDSHIP_RQ: 100, 
   NOTIFICATION_TYPE.WGNC_POP_UP: 500, 
   NOTIFICATION_TYPE.CLAN_APPS: 1, 
   NOTIFICATION_TYPE.CLAN_INVITES: 1, 
   NOTIFICATION_TYPE.CLAN_APP_ACTION: 500, 
   NOTIFICATION_TYPE.CLAN_INVITE_ACTION: 500, 
   NOTIFICATION_TYPE.CLAN_INVITE: 500, 
   NOTIFICATION_TYPE.CLAN_APP: 500, 
   NOTIFICATION_TYPE.PROGRESSIVE_REWARD: 1, 
   NOTIFICATION_TYPE.MISSING_EVENTS: 1, 
   NOTIFICATION_TYPE.CHOOSING_DEVICES: 5, 
   NOTIFICATION_TYPE.RECRUIT_REMINDER: 1, 
   NOTIFICATION_TYPE.EMAIL_CONFIRMATION_REMINDER: 1, 
   NOTIFICATION_TYPE.PSACOIN_REMINDER: 1, 
   NOTIFICATION_TYPE.GIFT_SYSTEM_OPERATION: 100, 
   NOTIFICATION_TYPE.NEW_YEAR_SPECIAL_LOOTBOXES: 1, 
   NOTIFICATION_TYPE.LUNAR_NY_ENVELOPES_RECEIVED: 1, 
   NOTIFICATION_TYPE.LUNAR_NY_NEW_ENVELOPES_RECEIVED: 1, 
   NOTIFICATION_TYPE.LUNAR_NY_NEW_ENVELOPES_RECEIVED_SIMPLE: 100}

class NOTIFICATION_BUTTON_STATE(object):
    HIDDEN = 0
    VISIBLE = 1
    ENABLED = 2
    WARNING = 4
    DEFAULT = VISIBLE | ENABLED


def makePathToIcon(iconName):
    result = ''
    if iconName:
        if iconName.startswith('img://'):
            result = iconName
        else:
            result = DEF_ICON_PATH.format(iconName)
    return result