# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBaseScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutBaseScorePanelMeta(BaseDAAPIComponent):

    def as_initS(self, maxValue, warningValue):
        if self._isDAAPIInited():
            return self.flashObject.as_init(maxValue, warningValue)

    def as_playScoreHighlightAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playScoreHighlightAnim()

    def as_stopScoreHighlightAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_stopScoreHighlightAnim()