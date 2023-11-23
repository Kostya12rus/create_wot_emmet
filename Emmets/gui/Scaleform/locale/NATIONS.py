# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/locale/NATIONS.py
from debug_utils import LOG_WARNING

class NATIONS(object):
    USSR = '#nations:ussr'
    GERMANY = '#nations:germany'
    USA = '#nations:usa'
    FRANCE = '#nations:france'
    UK = '#nations:uk'
    JAPAN = '#nations:japan'
    CZECH = '#nations:czech'
    CHINA = '#nations:china'
    POLAND = '#nations:poland'
    SWEDEN = '#nations:sweden'
    ITALY = '#nations:italy'
    USSR_GENETIVECASE = '#nations:ussr/genetiveCase'
    GERMANY_GENETIVECASE = '#nations:germany/genetiveCase'
    USA_GENETIVECASE = '#nations:usa/genetiveCase'
    CHINA_GENETIVECASE = '#nations:china/genetiveCase'
    FRANCE_GENETIVECASE = '#nations:france/genetiveCase'
    UK_GENETIVECASE = '#nations:uk/genetiveCase'
    JAPAN_GENETIVECASE = '#nations:japan/genetiveCase'
    CZECH_GENETIVECASE = '#nations:czech/genetiveCase'
    SWEDEN_GENETIVECASE = '#nations:sweden/genetiveCase'
    POLAND_GENETIVECASE = '#nations:poland/genetiveCase'
    ITALY_GENETIVECASE = '#nations:italy/genetiveCase'
    ALL_GENETIVECASE_ENUM = (
     USSR_GENETIVECASE,
     GERMANY_GENETIVECASE,
     USA_GENETIVECASE,
     CHINA_GENETIVECASE,
     FRANCE_GENETIVECASE,
     UK_GENETIVECASE,
     JAPAN_GENETIVECASE,
     CZECH_GENETIVECASE,
     SWEDEN_GENETIVECASE,
     POLAND_GENETIVECASE,
     ITALY_GENETIVECASE)
    ALL_ENUM = (
     USSR,
     GERMANY,
     USA,
     FRANCE,
     UK,
     JAPAN,
     CZECH,
     CHINA,
     POLAND,
     SWEDEN,
     ITALY,
     USSR_GENETIVECASE,
     GERMANY_GENETIVECASE,
     USA_GENETIVECASE,
     CHINA_GENETIVECASE,
     FRANCE_GENETIVECASE,
     UK_GENETIVECASE,
     JAPAN_GENETIVECASE,
     CZECH_GENETIVECASE,
     SWEDEN_GENETIVECASE,
     POLAND_GENETIVECASE,
     ITALY_GENETIVECASE)

    @classmethod
    def genetiveCase(cls, key0):
        outcome = ('#nations:{}/genetiveCase').format(key0)
        if outcome not in cls.ALL_GENETIVECASE_ENUM:
            LOG_WARNING(('Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def all(cls, key0):
        outcome = ('#nations:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING(('Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome