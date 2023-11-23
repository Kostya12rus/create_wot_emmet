# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/nations.py
NAMES = ('ussr', 'germany', 'usa', 'china', 'france', 'uk', 'japan', 'czech', 'sweden',
         'poland', 'italy')
INDICES = dict((n, i) for i, n in enumerate(NAMES))
MAP = {i: n for i, n in enumerate(NAMES)}
AVAILABLE_NAMES = ('ussr', 'germany', 'usa', 'china', 'france', 'uk', 'japan', 'czech',
                   'sweden', 'poland', 'italy')
NONE_INDEX = 15
ALL_NATIONS_INDEX = -1

class Alliances(object):
    USSR = 'Alliance-USSR'
    GERMANY = 'Alliance-Germany'
    USA = 'Alliance-USA'
    FRANCE = 'Alliance-France'


ALLIANCES_TAGS_ORDER = (
 Alliances.USSR, Alliances.GERMANY, Alliances.USA, Alliances.FRANCE)
ALLIANCES_TAGS = frozenset(ALLIANCES_TAGS_ORDER)
ALLIANCE_IDS = dict((value, index) for index, value in enumerate(ALLIANCES_TAGS_ORDER))
ALLIANCE_TO_NATIONS = {Alliances.USSR: frozenset(('ussr', 'china')), 
   Alliances.GERMANY: frozenset(('germany', 'japan')), 
   Alliances.USA: frozenset(('usa', 'uk', 'poland')), 
   Alliances.FRANCE: frozenset(('france', 'czech', 'sweden', 'italy'))}
ALLIANCE_IDS_MAP = {ai: set(INDICES[n] for n in ALLIANCE_TO_NATIONS[an]) for an, ai in ALLIANCE_IDS.iteritems()}
NATION_TO_ALLIANCE_IDS_MAP = {ni: ai for ni in ALLIANCE_IDS_MAP.iteritems()}