# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StoreViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onTabChange(self, tabId):
        self._printOverrideError('onTabChange')

    def onBackButtonClick(self):
        self._printOverrideError('onBackButtonClick')

    def as_showStorePageS(self, tabId):
        if self._isDAAPIInited():
            return self.flashObject.as_showStorePage(tabId)

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)

    def as_showBackButtonS(self, label, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackButton(label, description)

    def as_hideBackButtonS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBackButton()

    def as_setBtnTabCountersS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnTabCounters(counters)

    def as_removeBtnTabCountersS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_removeBtnTabCounters(counters)