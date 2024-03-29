# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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