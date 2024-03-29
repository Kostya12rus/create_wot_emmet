# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCSubtitlesWindow.py
from bootcamp.subtitles.subtitles import SubtitlesBase
from tutorial.gui.Scaleform.pop_ups import TutorialWindow
from gui.Scaleform.daapi.view.meta.SubtitlesWindowMeta import SubtitlesWindowMeta

class SubtitlesWindow(SubtitlesBase, SubtitlesWindowMeta, TutorialWindow):

    def onWindowClose(self):
        super(SubtitlesWindow, self).onWindowClose()
        self._onMouseClicked('closeID')
        self._stop()

    def _asShowSubtitle(self, subtitle):
        self.as_showSubtitleS(subtitle)

    def _asHideSubtitle(self):
        self.as_hideSubtitleS()

    def _stop(self):
        self._content.clear()
        if self._tutorial is not None:
            for _, effect in self._gui.effects.iterEffects():
                if effect.isStillRunning(self.uniqueName):
                    effect.stop()

        self.destroy()
        return