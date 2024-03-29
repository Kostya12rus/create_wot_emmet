# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCHighlightsMeta.py
from gui.Scaleform.framework.entities.View import View

class BCHighlightsMeta(View):

    def onComponentTriggered(self, highlightId):
        self._printOverrideError('onComponentTriggered')

    def onHighlightAnimationComplete(self, highlightId):
        self._printOverrideError('onHighlightAnimationComplete')

    def as_setDescriptorsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptors(data)

    def as_addHighlightS(self, highlightId):
        if self._isDAAPIInited():
            return self.flashObject.as_addHighlight(highlightId)

    def as_removeHighlightS(self, highlightId):
        if self._isDAAPIInited():
            return self.flashObject.as_removeHighlight(highlightId)