# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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