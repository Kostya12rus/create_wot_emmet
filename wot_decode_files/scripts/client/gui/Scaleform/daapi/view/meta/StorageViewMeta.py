# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StorageViewMeta(View):

    def navigateToHangar(self):
        self._printOverrideError('navigateToHangar')

    def onClose(self):
        self._printOverrideError('onClose')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_selectSectionS(self, sectionIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_selectSection(sectionIdx)

    def as_setButtonCounterS(self, sectionIdx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonCounter(sectionIdx, value)