# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ManualMainViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ManualMainViewMeta(View):

    def onChapterOpenedS(self, id):
        self._printOverrideError('onChapterOpenedS')

    def closeView(self):
        self._printOverrideError('closeView')

    def onBackButton(self):
        self._printOverrideError('onBackButton')

    def as_setChaptersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setChapters(data)

    def as_setPageBackgroundS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPageBackground(value)

    def as_showCloseBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showCloseBtn(value)

    def as_showBackBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackBtn(value)