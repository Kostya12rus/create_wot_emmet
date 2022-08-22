# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/goodies/goodie_constants.py
MAX_ACTIVE_GOODIES = 3

class GOODIE_STATE:
    INACTIVE = 0
    ACTIVE = 1
    USED = 2


class GOODIE_VARIETY:
    DISCOUNT = 0
    BOOSTER = 1
    DEMOUNT_KIT = 2
    RECERTIFICATION_FORM = 3
    DISCOUNT_NAME = 'discount'
    BOOSTER_NAME = 'booster'
    DEMOUNT_KIT_NAME = 'demountKit'
    RECERTIFICATION_FORM_NAME = 'recertificationForm'
    NAME_TO_ID = {DISCOUNT_NAME: DISCOUNT, 
       BOOSTER_NAME: BOOSTER, 
       DEMOUNT_KIT_NAME: DEMOUNT_KIT, 
       RECERTIFICATION_FORM_NAME: RECERTIFICATION_FORM}
    DISCOUNT_LIKE = (
     DISCOUNT,
     DEMOUNT_KIT,
     RECERTIFICATION_FORM)


class GOODIE_TARGET_TYPE:
    ON_BUY_PREMIUM = 1
    ON_BUY_SLOT = 2
    ON_POST_BATTLE = 3
    ON_BUY_GOLD_TANKMEN = 4
    ON_FREE_XP_CONVERSION = 5
    ON_BUY_VEHICLE = 6
    ON_EPIC_META = 7
    ON_DEMOUNT_OPTIONAL_DEVICE = 8
    EPIC_POST_BATTLE = 9
    ON_DROP_SKILL = 10


class GOODIE_CONDITION_TYPE:
    MAX_VEHICLE_LEVEL = 1


class GOODIE_RESOURCE_TYPE:
    GOLD = 10
    CREDITS = 20
    XP = 30
    CREW_XP = 40
    FREE_XP = 50
    FL_XP = 60


class GOODIE_NOTIFICATION_TYPE:
    EMPTY = 1
    REMOVED = 3
    DISABLED = 4
    ENABLED = 5