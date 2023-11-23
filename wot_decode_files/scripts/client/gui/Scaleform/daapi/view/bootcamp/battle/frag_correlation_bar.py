# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/battle/frag_correlation_bar.py
from bootcamp.BootCampEvents import g_bootcampEvents
from gui.Scaleform.daapi.view.meta.BCFragCorrelationBarMeta import BCFragCorrelationBarMeta
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES

class BootcampFragCorrelationBar(BCFragCorrelationBarMeta):

    def __init__(self):
        super(BootcampFragCorrelationBar, self).__init__()
        self.__needHint = False

    def _populate(self):
        super(BootcampFragCorrelationBar, self)._populate()
        g_bootcampEvents.onHighlightAdded += self.__onHighlightAdded

    def _dispose(self):
        g_bootcampEvents.onHighlightAdded -= self.__onHighlightAdded
        super(BootcampFragCorrelationBar, self)._dispose()

    def __onHighlightAdded(self, alias):
        if alias == BATTLE_VIEW_ALIASES.FRAG_CORRELATION_BAR:
            self.as_showHintS()