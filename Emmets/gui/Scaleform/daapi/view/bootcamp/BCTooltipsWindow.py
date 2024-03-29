# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCTooltipsWindow.py
from gui.Scaleform.daapi.view.meta.BCTooltipsWindowMeta import BCTooltipsWindowMeta
from uilogging.deprecated.decorators import loggerTarget, loggerEntry, logOnMatch
from uilogging.deprecated.bootcamp.constants import BC_LOG_KEYS, HANGAR_HINTS_TO_LOG_ON_COMPLETE
from uilogging.deprecated.bootcamp.loggers import BootcampUILogger

@loggerTarget(logKey=BC_LOG_KEYS.BC_HANGAR_HINTS, loggerCls=BootcampUILogger)
class BCTooltipsWindow(BCTooltipsWindowMeta):

    def __init__(self, settings):
        super(BCTooltipsWindow, self).__init__()
        self.__completed = settings['completed']
        self.__hideCallback = settings['hideCallback']
        self._tooltip_id = settings['id']

    def animFinish(self):
        if self.__hideCallback is not None:
            self.__hideCallback()
        return

    @property
    def tooltip_id(self):
        return self._tooltip_id

    @loggerEntry
    def _populate(self):
        super(BCTooltipsWindow, self)._populate()
        if self.__completed:
            self.as_completeHandlerS()
        else:
            self.as_showHandlerS()

    @logOnMatch(objProperty='tooltip_id', matches=HANGAR_HINTS_TO_LOG_ON_COMPLETE)
    def as_completeHandlerS(self):
        super(BCTooltipsWindow, self).as_completeHandlerS()