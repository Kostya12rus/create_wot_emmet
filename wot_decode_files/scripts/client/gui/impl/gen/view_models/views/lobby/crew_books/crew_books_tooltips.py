# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew_books/crew_books_tooltips.py
from frameworks.wulf import ViewModel

class CrewBooksTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_CREW_BOOK_RESTRICTED = 'crewBookRestricted'
    TOOLTIP_TANKMAN = 'tankman'
    TOOLTIP_TANKMAN_NEW_SKILL = 'tankmanNewSkill'
    TOOLTIP_TANKMAN_SKILL = 'tankmanSkill'

    def __init__(self, properties=0, commands=0):
        super(CrewBooksTooltips, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CrewBooksTooltips, self)._initialize()