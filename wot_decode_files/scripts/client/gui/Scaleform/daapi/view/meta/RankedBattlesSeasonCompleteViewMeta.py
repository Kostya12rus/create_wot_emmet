# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesSeasonCompleteViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesSeasonCompleteViewMeta(WrapperViewMeta):

    def showRating(self):
        self._printOverrideError('showRating')

    def closeView(self):
        self._printOverrideError('closeView')

    def onSoundTrigger(self, soundName):
        self._printOverrideError('onSoundTrigger')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setPlaceS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlace(value)

    def as_setAwardsDataS(self, awardsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardsData(awardsData)