# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_pagination.py
import Event
from gui.Scaleform.daapi.view.meta.PaginationMeta import PaginationMeta
from gui.shared.formatters import text_styles

class EventBoardsPagination(PaginationMeta):

    def __init__(self):
        super(EventBoardsPagination, self).__init__()
        self.onStepPage = Event.Event()

    def showPage(self, direction):
        self.onStepPage(direction)

    def updatePage(self, page, pagesAmount):
        self.as_setPageS(('{} / {}').format(text_styles.highTitle(page), pagesAmount))
        self.as_setEnabledS(page > 1, page < pagesAmount)