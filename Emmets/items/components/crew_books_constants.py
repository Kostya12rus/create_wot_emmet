# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/crew_books_constants.py
CREW_BOOKS_XML_FILE = 'crewBooks.xml'
CREW_BOOKS_PRICE_GROUPS_XML_FILE = 'priceGroups.xml'
CREW_BOOK_TYPES_XML_FILE = 'crewBookTypes.xml'
CREW_BOOK_DISPLAYED_AWARDS_COUNT = 11

class CREW_BOOK_PROPERTIES_MASKS:
    FULL_CREW = 1
    ROLE_LEVEL = 2
    SPECIALIZATION = 4
    EMPTY_MASK = 0
    ALL = (
     FULL_CREW, ROLE_LEVEL, SPECIALIZATION)


class CrewBookCacheType:
    CREW_BOOK = 1
    ITEM_GROUP = 2
    RANGE = {
     CREW_BOOK, ITEM_GROUP}


class CREW_BOOK_RARITY:
    CREW_COMMON = 'brochure'
    CREW_RARE = 'guide'
    CREW_EPIC = 'crewBook'
    PERSONAL = 'personalBook'
    UNIVERSAL = 'universalBook'
    ALL_TYPES = (
     CREW_COMMON, CREW_RARE, CREW_EPIC, PERSONAL, UNIVERSAL)
    NO_NATION_TYPES = (PERSONAL, UNIVERSAL)
    ORDER = dict(zip(ALL_TYPES, range(len(ALL_TYPES))))


class CREW_BOOK_SPREAD:
    CREW_BOOK = 'crewBook'
    PERSONAL_BOOK = 'personalBook'
    CREW_BOOK_NO_NATION = 'universalBook'
    ALL_SPREADS = (
     CREW_BOOK, PERSONAL_BOOK, CREW_BOOK_NO_NATION)


class CREW_BOOK_INVALID_TYPE(object):
    EMPTY_CREW = 'emptyCrew'
    INCOMPLETE_CREW = 'incompleteCrew'
    INVALID_SPECIALITY = 'invalidSpeciality'
    INVALID_SKILL = 'invalidSkill'


CREW_BOOK_RESTRICTIONS = {CREW_BOOK_PROPERTIES_MASKS.ROLE_LEVEL: CREW_BOOK_INVALID_TYPE.INVALID_SKILL, 
   CREW_BOOK_PROPERTIES_MASKS.SPECIALIZATION: CREW_BOOK_INVALID_TYPE.INVALID_SPECIALITY, 
   CREW_BOOK_PROPERTIES_MASKS.FULL_CREW: CREW_BOOK_INVALID_TYPE.INCOMPLETE_CREW}