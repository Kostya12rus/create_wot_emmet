# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseStorageCategoryViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseStorageCategoryViewMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError('setActiveState')

    def playInfoSound(self):
        self._printOverrideError('playInfoSound')

    def scrolledToBottom(self):
        self._printOverrideError('scrolledToBottom')

    def as_showDummyScreenS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showDummyScreen(show)

    def as_showFilterWarningS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterWarning(data)

    def as_getCardsDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCardsDP()

    def as_scrollToItemS(self, itemIntCD):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToItem(itemIntCD)