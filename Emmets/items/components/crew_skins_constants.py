# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/crew_skins_constants.py
CREW_SKINS_XML_FILE = 'crewSkins.xml'
CREW_SKINS_PRICE_GROUPS_XML_FILE = 'priceGroups.xml'
NO_CREW_SKIN_ID = 0
NO_CREW_SKIN_SOUND_SET = '-'

class CREW_SKIN_PROPERTIES_MASKS:
    ROLE = 1
    SEX = 2
    NATION = 4
    EMPTY_MASK = 0


class CrewSkinType:
    CREW_SKIN = 1
    ITEM_GROUP = 2
    RANGE = {
     CREW_SKIN, ITEM_GROUP}


class TANKMAN_SEX:
    NONE = ''
    MALE = 'male'
    FEMALE = 'female'
    ALL = (
     MALE, FEMALE)
    AVAILABLE = (NONE, MALE, FEMALE)

    @staticmethod
    def getTankmanSex(tmanDescr):
        if tmanDescr.isFemale:
            return TANKMAN_SEX.FEMALE
        return TANKMAN_SEX.MALE


class CREW_SKIN_RARITY:
    COMMON = 1
    RARE = 2
    EPIC = 3
    ALL = (
     COMMON, RARE, EPIC)