# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventPlayerPackTradeMeta.py
from gui.Scaleform.framework.entities.View import View

class EventPlayerPackTradeMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def backView(self):
        self._printOverrideError('backView')

    def onButtonPaymentSetPanelClick(self, count):
        self._printOverrideError('onButtonPaymentSetPanelClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)