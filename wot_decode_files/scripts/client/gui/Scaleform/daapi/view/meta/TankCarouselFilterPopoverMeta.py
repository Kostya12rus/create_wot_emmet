# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselFilterPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class TankCarouselFilterPopoverMeta(SmartPopOverView):

    def changeFilter(self, groupId, itemId):
        self._printOverrideError('changeFilter')

    def changeSearchNameVehicle(self, inputText):
        self._printOverrideError('changeSearchNameVehicle')

    def switchCarouselType(self, selected):
        self._printOverrideError('switchCarouselType')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)

    def as_showCounterS(self, countText):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText)