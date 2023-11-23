# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_matters/battle_matters_constants.py
from enum import Enum
CARDS_CONFIG_XML_PATH = 'gui/battle_matters_cards.xml'

class QuestCardSections(Enum):
    ID = 'id'
    SWF_PATH = 'swfPath'
    LESSON_ID = 'lessonId'


class SequenceNumber(Enum):
    SINGLE = 0
    FIRST = 1
    MIDDLE = 2
    LAST = 3