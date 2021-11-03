# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ChannelCarouselMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelCarouselMeta(BaseDAAPIComponent):

    def channelOpenClick(self, itemID):
        self._printOverrideError('channelOpenClick')

    def closeAll(self):
        self._printOverrideError('closeAll')

    def channelCloseClick(self, itemID):
        self._printOverrideError('channelCloseClick')

    def updateItemDataFocus(self, itemID, wndType, isFocusIn):
        self._printOverrideError('updateItemDataFocus')

    def updateItemDataOpened(self, itemID, wndType, isWindowOpened):
        self._printOverrideError('updateItemDataOpened')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_getBattlesDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getBattlesDataProvider()