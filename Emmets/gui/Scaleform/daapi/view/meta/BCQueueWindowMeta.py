# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCQueueWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCQueueWindowMeta(View):

    def cancel(self):
        self._printOverrideError('cancel')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_showCancelButtonS(self, value, label, info):
        if self._isDAAPIInited():
            return self.flashObject.as_showCancelButton(value, label, info)

    def as_setStatusTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusText(value)