# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageCarouselEnvironmentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StorageCarouselEnvironmentMeta(BaseDAAPIComponent):

    def resetFilter(self):
        self._printOverrideError('resetFilter')

    def showItemInfo(self, itemId):
        self._printOverrideError('showItemInfo')

    def changeSearchNameVehicle(self, inputText):
        self._printOverrideError('changeSearchNameVehicle')

    def as_updateSearchS(self, searchInputLabel, searchInputName, searchInputTooltip, searchInputMaxChars):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSearch(searchInputLabel, searchInputName, searchInputTooltip, searchInputMaxChars)

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)