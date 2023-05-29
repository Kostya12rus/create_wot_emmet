# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew_books/crew_books_tooltips.py
from frameworks.wulf import ViewModel

class CrewBooksTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_CREW_BOOK_RESTRICTED = 'crewBookRestricted'
    TOOLTIP_TANKMAN = 'tankman'
    TOOLTIP_TANKMAN_NEW_SKILL = 'tankmanNewSkill'
    TOOLTIP_TANKMAN_SKILL = 'crewPerkGf'

    def __init__(self, properties=0, commands=0):
        super(CrewBooksTooltips, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CrewBooksTooltips, self)._initialize()