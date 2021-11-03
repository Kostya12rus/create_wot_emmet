# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCOutroVideoPage.py
from gui.Scaleform.daapi.view.bootcamp.BCVideoPage import BCVideoPage
from tutorial.gui.Scaleform.pop_ups import TutorialDialog
from uilogging.deprecated.decorators import loggerTarget, loggerEntry, simpleLog
from uilogging.deprecated.bootcamp.constants import BC_LOG_ACTIONS, BC_LOG_KEYS
from uilogging.deprecated.bootcamp.loggers import BootcampUILogger

@loggerTarget(logKey=BC_LOG_KEYS.BC_OUTRO_VIDEO, loggerCls=BootcampUILogger)
class BCOutroVideoPage(BCVideoPage, TutorialDialog):
    _DEFAULT_MASTER_VOLUME = 0.5

    def cancel(self):
        self._onMouseClicked('cancelID')
        self._onFinish()

    @simpleLog(action=BC_LOG_ACTIONS.SKIP_VIDEO)
    def _onDestroy(self):
        self.onDispose -= self.__onDispose
        self._content.clear()
        if self._tutorial is not None:
            for _, effect in self._gui.effects.iterEffects():
                if effect.isStillRunning(self.uniqueName):
                    effect.stop(effectID=None)

        return

    @loggerEntry
    def _populate(self):
        self.onDispose += self.__onDispose
        BCVideoPage._populate(self)

    def __onDispose(self, dispoableEntity):
        if self is dispoableEntity:
            self.cancel()