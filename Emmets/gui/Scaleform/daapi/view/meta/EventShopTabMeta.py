# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventShopTabMeta.py
from gui.Scaleform.framework.entities.View import View

class EventShopTabMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onItemsBannerClick(self):
        self._printOverrideError('onItemsBannerClick')

    def onMainBannerClick(self):
        self._printOverrideError('onMainBannerClick')

    def onPackBannerClick(self, id):
        self._printOverrideError('onPackBannerClick')

    def as_setPackBannersDataS(self, dataPack1, dataPack2):
        if self._isDAAPIInited():
            return self.flashObject.as_setPackBannersData(dataPack1, dataPack2)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_setExpireDateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setExpireDate(value)