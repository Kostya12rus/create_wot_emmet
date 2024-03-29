# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/locale/EVENT.py
from debug_utils import LOG_WARNING

class EVENT(object):
    PUNISHMENTWINDOW_REASON_EVENT_DESERTER = '#event:punishmentWindow/reason/event_deserter'
    PUNISHMENTWINDOW_REASON_EVENT_AFK = '#event:punishmentWindow/reason/event_afk'
    BATTLEHINTS_TESTMESSAGE = '#event:battleHints/testMessage'
    BATTLEHINTS_TESTMESSAGEWITHPARAMS = '#event:battleHints/testMessageWithParams'
    CRAFTMACHINE_TITLE = '#event:craftMachine/title'
    CRAFTMACHINE_SUBTITLE = '#event:craftMachine/subTitle'
    CRAFTMACHINE_ENDDATETEXT = '#event:craftMachine/endDateText'
    ALL_ENUM = (
     PUNISHMENTWINDOW_REASON_EVENT_DESERTER,
     PUNISHMENTWINDOW_REASON_EVENT_AFK,
     BATTLEHINTS_TESTMESSAGE,
     BATTLEHINTS_TESTMESSAGEWITHPARAMS,
     CRAFTMACHINE_TITLE,
     CRAFTMACHINE_SUBTITLE,
     CRAFTMACHINE_ENDDATETEXT)

    @classmethod
    def all(cls, key0):
        outcome = ('#event:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING(('Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome